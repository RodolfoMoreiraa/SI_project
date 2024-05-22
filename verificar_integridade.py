import os
import shutil
import logging
from time import sleep
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import hashlib

# Configurar logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class IntegrityHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            self.verify_integrity(event.src_path)

    def verify_integrity(self, file_path):
        if not file_path.endswith('.hash'):
            logging.debug(f"Ignorando arquivo não hash: {file_path}")
            return

        base_name = os.path.basename(file_path).rsplit('.', 1)[0]
        data_file_path = os.path.join('Integrity', base_name)

        if not os.path.exists(data_file_path):
            logging.error(f"Arquivo original não encontrado: {data_file_path}")
            return

        attempts = 5
        for attempt in range(attempts):
            try:
                with open(file_path, 'r') as f:
                    expected_hash = f.read().strip()
                    logging.debug(f"Hash esperado lido do arquivo {file_path}: {expected_hash}")

                with open(data_file_path, 'rb') as f:
                    data = f.read()
                    h = hashlib.sha256(data)

                calculated_hash = h.hexdigest()
                logging.debug(f"Hash calculado para {data_file_path}: {calculated_hash}")

                if calculated_hash == expected_hash:
                    shutil.move(data_file_path, 'Integrity_Valid')
                    shutil.move(file_path, 'Integrity_Valid')
                    logging.info(f"Verificação válida para a integridade do arquivo {data_file_path}")
                else:
                    shutil.move(data_file_path, 'Integrity_NotValid')
                    shutil.move(file_path, 'Integrity_NotValid')
                    logging.warning(f"Verificação inválida para a integridade do arquivo {data_file_path}")
                break
            except Exception as e:
                logging.error(f"Tentativa {attempt+1}/{attempts} falhou: {e}")
                if attempt < attempts - 1:
                    sleep(1)
                else:
                    logging.critical(f"Erro persistente ao verificar a integridade do arquivo {file_path} após {attempts} tentativas.")

def monitor_folder(folder_name, handler_class):
    observer = Observer()
    event_handler = handler_class()
    observer.schedule(event_handler, path=folder_name, recursive=False)
    observer.start()
    logging.info(f"Estamos a monitorizar a pasta '{folder_name}'.")
    try:
        while True:
            sleep(30)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    folders = ['Integrity', 'Integrity_Valid', 'Integrity_NotValid']
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)

    monitor_folder('Integrity', IntegrityHandler)
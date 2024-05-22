import os
import shutil
from time import sleep
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

class VerifyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            self.verify_file(event.src_path)

    def verify_file(self, file_path):
        if not file_path.endswith('.sig'):
            return

        base_name = os.path.basename(file_path).rsplit('.', 1)[0]
        data_file_path = os.path.join('Verify', base_name)
        public_key_path = os.path.join('Verify', 'public-key-file.pem')

        if not os.path.exists(data_file_path) or not os.path.exists(public_key_path):
            print("Arquivo ou chave pública não encontrados!")
            return

        with open(public_key_path, 'rb') as f:
            public_key = RSA.import_key(f.read())

        with open(data_file_path, 'rb') as f:
            data = f.read()
        h = SHA256.new(data)

        with open(file_path, 'rb') as f:
            signature = f.read()

        try:
            pkcs1_15.new(public_key).verify(h, signature)
            shutil.move(data_file_path, 'Valid_Sign')
            shutil.move(file_path, 'Valid_Sign')
            print(f"Assinatura válida: {data_file_path}")
        except (ValueError, TypeError):
            shutil.move(data_file_path, 'NotValid_Sign')
            shutil.move(file_path, 'NotValid_Sign')
            print(f"Assinatura inválida: {data_file_path}")

def monitor_folder(folder_name, handler_class):
    observer = Observer()
    event_handler = handler_class()
    observer.schedule(event_handler, path=folder_name, recursive=False)
    observer.start()
    print(f"Estamos a monitorizar a pasta '{folder_name}'.")
    try:
        while True:
            sleep(30)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    folders = ['Verify', 'Valid_Sign', 'NotValid_Sign']
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)

    monitor_folder('Verify', VerifyHandler)


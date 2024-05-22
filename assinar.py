import os
import shutil
from time import sleep
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

class SignHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            self.sign_file(event.src_path)

    def sign_file(self, file_path):
        # Verificar se a chave privada está presente
        private_key_path = os.path.join('Sign', 'private-key-file.pem')
        if not os.path.exists(private_key_path):
            print("Chave privada não encontrada!")
            return

        # Verificar se o arquivo é a chave privada para evitar assiná-lo
        if os.path.basename(file_path) == 'private-key-file.pem':
            return

        # Ler a chave privada
        with open(private_key_path, 'rb') as f:
            private_key = RSA.import_key(f.read())

        # Ler o arquivo a ser assinado
        with open(file_path, 'rb') as f:
            data = f.read()
        h = SHA256.new(data)
        signature = pkcs1_15.new(private_key).sign(h)

        # Salvar a assinatura na pasta 'Assinado'
        sig_file_path = os.path.join('Assinado', os.path.basename(file_path) + '.sig')
        with open(sig_file_path, 'wb') as f:
            f.write(signature)

        # Mover o arquivo original para a pasta 'Signed'
        shutil.move(file_path, os.path.join('Assinado', os.path.basename(file_path)))

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
    folders = ['Sign', 'Assinado']
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)

    monitor_folder('Sign', SignHandler)


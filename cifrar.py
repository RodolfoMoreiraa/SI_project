import os
import shutil
from time import sleep
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

class EncryptHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            self.encrypt_file(event.src_path)

    def encrypt_file(self, file_path):
        key = get_random_bytes(16)
        iv = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        with open(file_path, 'rb') as f:
            data = f.read()
        padded_data = data + b"\0" * (AES.block_size - len(data) % AES.block_size)
        encrypted_data = cipher.encrypt(padded_data)

        enc_file_path = os.path.join('Encrypted', os.path.basename(file_path))
        with open(enc_file_path, 'wb') as f:
            f.write(encrypted_data)

        key_file_path = os.path.join('Encrypted', 'key-file.txt')
        iv_file_path = os.path.join('Encrypted', 'iv-file.txt')
        with open(key_file_path, 'wb') as f:
            f.write(key)
        with open(iv_file_path, 'wb') as f:
            f.write(iv)

        os.remove(file_path)

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
    folders = ['Encrypt', 'Encrypted']
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)

    monitor_folder('Encrypt', EncryptHandler)

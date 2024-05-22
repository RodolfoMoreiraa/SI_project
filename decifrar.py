import os
import shutil
from time import sleep
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from Crypto.Cipher import AES

class DecryptHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            self.decrypt_file(event.src_path)

    def decrypt_file(self, file_path):
        base_name = os.path.basename(file_path)
        encrypted_folder = 'Encrypted'
        key_file_path = os.path.join(encrypted_folder, 'key-file.txt')
        iv_file_path = os.path.join(encrypted_folder, 'iv-file.txt')

        if os.path.exists(key_file_path) and os.path.exists(iv_file_path):
            with open(key_file_path, 'rb') as f:
                key = f.read()
            with open(iv_file_path, 'rb') as f:
                iv = f.read()

            cipher = AES.new(key, AES.MODE_CBC, iv)
            with open(file_path, 'rb') as f:
                encrypted_data = f.read()
            decrypted_data = cipher.decrypt(encrypted_data).rstrip(b"\0")

            decrypted_folder = 'Decrypted'
            dec_file_path = os.path.join(decrypted_folder, base_name)
            with open(dec_file_path, 'wb') as f:
                f.write(decrypted_data)

            os.remove(file_path)

def monitor_folder(folder_name, handler_class):
    observer = Observer()
    event_handler = handler_class()
    observer.schedule(event_handler, path=folder_name, recursive=False)
    observer.start()
    print(f"Monitorando a pasta '{folder_name}'.")
    try:
        while True:
            sleep(30)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    folders = ['Decrypt', 'Decrypted']
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)

    monitor_folder('Decrypt', DecryptHandler)

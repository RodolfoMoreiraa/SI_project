import os
import shutil
from time import sleep
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from Crypto.Hash import SHA256

class DigestHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            self.digest_file(event.src_path)

    def digest_file(self, file_path):
        with open(file_path, 'rb') as f:
            data = f.read()
        h = SHA256.new(data)
        hash_file_path = os.path.join('Hashes', os.path.basename(file_path) + '.hash')
        with open(hash_file_path, 'w') as f:
            f.write(h.hexdigest())

        shutil.move(file_path, 'Hashes')

def monitor_folder(folder_name, handler_class):
    observer = Observer()
    event_handler = handler_class()
    observer.schedule(event_handler, path=folder_name, recursive=False)
    observer.start()
    print(f"Estamos a Monitorizar a pasta '{folder_name}'.")
    try:
        while True:
            sleep(30)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    folders = ['Digest', 'Hashes']
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)

    monitor_folder('Digest', DigestHandler)


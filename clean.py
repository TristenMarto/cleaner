import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for file in os.listdir(folder):
            tracking_path = os.path.join(folder,file)
            if not file.startswith('.') and os.path.isfile(tracking_path) == True:
                x, y = os.path.splitext(file)[0].split("- ")
                final_directory = os.path.join(folder, y)
                os.makedirs(final_directory)
                final_file_path = final_directory + "/" + "kvk_" + file
                os.rename(tracking_path, final_file_path)
            
        


folder = '/Users/tristen.assenmacher/Desktop/Checks'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder, recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()

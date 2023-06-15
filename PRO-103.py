import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Set the path for the directory to track changes
from_dir = "<Set path for tracking file system events>"

# Define a custom FileEventHandler class
class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print("File Created:", event.src_path)
        
    def on_modified(self, event):
        print("File Modified:", event.src_path)
        
    def on_moved(self, event):
        print("File Moved:", event.src_path)
        
    def on_deleted(self, event):
        print("File Deleted:", event.src_path)

# Set the observer to watch the changes
event_handler = FileEventHandler()
observer = Observer()
observer.schedule(event_handler, from_dir, recursive=True)
observer.start()

try:
    # Add the code to stop the observer program when any key is pressed
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()

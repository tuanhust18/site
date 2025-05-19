import time
import webbrowser
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import subprocess

CSV_FILE = r"C:\Users\ThanhTuanNguyen\Desktop\publications.csv"
GENERATE_SCRIPT = r"C:\Users\ThanhTuanNguyen\Documents\GitHub\site\generate_publications.py"
HTML_OUTPUT = "publications.html"

class PublicationHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith("publications.csv"):
            print("📄 CSV file updated. Regenerating HTML...")
            subprocess.run(["python", GENERATE_SCRIPT], check=True)
            html_path = os.path.abspath(HTML_OUTPUT)
            webbrowser.open(f"file:///{html_path}")
            print("✅ HTML updated and opened in browser.\n")

if __name__ == "__main__":
    path = os.path.dirname(CSV_FILE)
    event_handler = PublicationHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path, recursive=False)
    observer.start()
    print("👀 Watching for changes in publications.csv...\nPress Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

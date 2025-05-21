import time
import webbrowser
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import subprocess

CSV_FILE = r"C:\Users\ThanhTuanNguyen\Documents\GitHub\site\publications.csv"
GENERATE_SCRIPT = r"C:\Users\ThanhTuanNguyen\Documents\GitHub\site\generate_publications.py"
HTML_OUTPUT = "publications.html"
REPO_DIR = r"C:\Users\ThanhTuanNguyen\Documents\GitHub\site"  # Thư mục chứa repo Git

class PublicationHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith("publications.csv"):
            print("📄 CSV file updated. Regenerating HTML...")
            subprocess.run(["python", GENERATE_SCRIPT], check=True)

            # Auto push to GitHub
            try:
                print("🚀 Committing and pushing to GitHub...")
                subprocess.run(["git", "add", HTML_OUTPUT], cwd=REPO_DIR, check=True)
                subprocess.run(["git", "commit", "-m", "🔄 Auto-update publications"], cwd=REPO_DIR, check=True)
                subprocess.run(["git", "push"], cwd=REPO_DIR, check=True)
                print("✅ GitHub updated.\n")
            except subprocess.CalledProcessError as e:
                print("❌ Git push failed:", e)

            # Optional: open HTML
            html_path = os.path.abspath(os.path.join(REPO_DIR, HTML_OUTPUT))
            webbrowser.open(f"file:///{html_path}")

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

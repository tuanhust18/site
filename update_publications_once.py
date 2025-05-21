import os
import subprocess
from generate_publications import load_publications, sort_publications, generate_html, save_html

# 1. Tạo HTML từ CSV
csv_file = r"C:\Users\ThanhTuanNguyen\Documents\GitHub\site\publications.csv"
html_file = "publications.html"

publications = load_publications(csv_file)
publications_sorted = sort_publications(publications)
html_output = generate_html(publications_sorted)
save_html(html_output, html_file)

# 2. Kiểm tra nếu publications.html có thay đổi
result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
if html_file in result.stdout:
    print("📄 Changes detected in publications.html. Committing and pushing to GitHub...")

    # 3. Thêm, commit, push
    subprocess.run(["git", "add", html_file])
    subprocess.run(["git", "commit", "-m", "🔄 Update publications"])
    subprocess.run(["git", "push"])
    print("✅ Pushed to GitHub successfully.")
else:
    print("🟢 No changes in publications.html. Nothing to commit.")

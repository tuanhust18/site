import requests

author_id = "V3Qc_HsAAAAJ"
api_key = "d83574e9881757768965d462eec78a446bd242b633b1f73378539004988be08c"

url = f"https://serpapi.com/search.json?engine=google_scholar_author&author_id={author_id}&api_key={api_key}"

response = requests.get(url)
if response.status_code != 200:
    print("Failed to get data:", response.status_code)
    exit(1)

data = response.json()

articles = data.get("articles", [])

html_parts = []
html_parts.append("""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Publications</title>
<style>
  body { font-family: Arial, sans-serif; padding: 20px; max-width: 800px; margin: auto; }
  h1 { text-align: center; }
  .pub { margin-bottom: 20px; padding: 10px; border: 1px solid #ddd; border-radius: 5px; }
  .title { font-weight: bold; font-size: 1.1em; }
  .details { font-size: 0.9em; color: #555; }
</style>
</head>
<body>
<h1>Google Scholar Publications</h1>
""")

if not articles:
    html_parts.append("<p>No publications found.</p>")
else:
    for pub in articles:
        title = pub.get("title", "No title")
        authors = pub.get("authors", "Unknown authors")
        publication = pub.get("publication", "Unknown publication")
        year = pub.get("year", "")
        html_parts.append(f"""
        <div class="pub">
            <div class="title">{title}</div>
            <div class="details">{authors} – {publication} ({year})</div>
        </div>
        """)

html_parts.append("""
</body>
</html>
""")

html_content = "\n".join(html_parts)

with open("publications.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("File publications.html đã được tạo thành công!")

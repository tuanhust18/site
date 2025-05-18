import csv

def load_publications(csv_path):
    publications = []
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            title = row.get('title', '').strip()
            if not title:
                continue  # Bỏ qua nếu không có tiêu đề
            try:
                row['year'] = int(row.get('year', '').strip())
            except:
                row['year'] = None
            publications.append(row)
    return publications

def sort_publications(publications):
    return sorted(publications, key=lambda x: x['year'] or 0, reverse=True)

def generate_html(publications):
    list_items = ""
    for idx, pub in enumerate(publications, 1):
        title = pub.get('title', '').strip()
        authors = pub.get('authors', 'N/A').strip()
        highlight_name = "Thanh Tuan Nguyen"
        authors = authors.replace(highlight_name, f"<strong>{highlight_name}</strong>")

        journal = pub.get('journal', '').strip()
        year = pub.get('year')
        volume = pub.get('volume', '').strip()
        issue = pub.get('issue', '').strip()
        pages = pub.get('pages', '').strip()
        doi = pub.get('doi', '').strip()
        pdf_link = pub.get('pdf_link', '').strip()

        meta_badges = []
        if year:
            meta_badges.append(f'<span class="badge bg-secondary">{year}</span>')
        if volume:
            meta_badges.append(f'<span class="badge bg-info text-dark">Vol. {volume}</span>')
        if issue:
            meta_badges.append(f'<span class="badge bg-warning text-dark">Issue {issue}</span>')
        if pages:
            meta_badges.append(f'<span class="badge bg-success">pp. {pages}</span>')
        if journal:
            journal_str = f'<em>{journal}</em>'
        else:
            journal_str = ""

        links = []
        if doi:
            links.append(f'🔗 <a href="https://doi.org/{doi}" target="_blank">DOI</a>')
        if pdf_link:
            links.append(f'📄 <a href="{pdf_link}" target="_blank">PDF</a>')
        links_str = ' | '.join(links)

        list_items += f"""
        <li class="list-group-item shadow-sm p-4 mb-3 bg-white rounded publication-item">
            <div class="d-flex justify-content-between align-items-start">
                <h5 class="fw-bold">{idx}. {title}</h5>
                <div>{''.join(meta_badges)}</div>
            </div>
            <p class="mb-1"><strong>Authors:</strong> {authors}</p>
            <p class="mb-1">{journal_str}</p>
            <p class="text-muted small">{links_str}</p>
        </li>"""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Publications</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {{
            padding: 2rem;
            background-color: #f0f2f5;
        }}
        h2 {{
            margin-bottom: 2rem;
            font-weight: bold;
        }}
        .publication-item:hover {{
            background-color: #eef5ff;
            transition: 0.3s;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h2>📚 Publications</h2>
        <ul class="list-group list-group-flush">
            {list_items}
        </ul>
    </div>
</body>
</html>"""
    return html



def save_html(html_content, filename="publications.html"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"✅ HTML exported to {filename}")

if __name__ == "__main__":
    csv_file = r"C:\Users\ThanhTuanNguyen\Desktop\publications.csv"
    publications = load_publications(csv_file)
    publications_sorted = sort_publications(publications)
    html_output = generate_html(publications_sorted)
    save_html(html_output)

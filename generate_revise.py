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
    # Sắp xếp giảm dần theo năm (mới đến cũ)
    return sorted(publications, key=lambda x: x['year'] or 0, reverse=True)

def generate_html(publications):
    list_items = ""
    highlight_name = "Thanh Tuan Nguyen"
    total = len(publications)
    for idx, pub in enumerate(publications):
        display_idx = total - idx  # đánh số ngược

        title = pub.get('title', '').strip()
        authors = pub.get('authors', 'N/A').strip()
        authors = authors.replace(highlight_name, f'<strong style="color:#4fc3f7;">{highlight_name}</strong>')

        journal = pub.get('journal', '').strip()
        year = pub.get('year')
        volume = pub.get('volume', '').strip()
        issue = pub.get('issue', '').strip()
        pages = pub.get('pages', '').strip()
        doi = pub.get('doi', '').strip()
        pdf_link = pub.get('pdf_link', '').strip()

        details = []
        if journal:
            details.append(f"<em>{journal}</em>")
        if year:
            details.append(str(year))
        if volume:
            details.append(f"Vol. {volume}")
        if issue:
            details.append(f"Issue {issue}")
        if pages:
            details.append(f"pp. {pages}")
        details_str = ', '.join(details)

        links = []
        if doi:
            links.append(f'🔗 <a href="https://doi.org/{doi}" target="_blank">DOI</a>')
        if pdf_link:
            links.append(f'📄 <a href="{pdf_link}" target="_blank">PDF</a>')
        links_str = ' | '.join(links)

        list_items += f"""
        <li class="list-group-item mb-3">
            <h5 class="mb-1 publication-title">{display_idx}. {title}</h5>
            <p class="mb-1"><strong>Authors:</strong> {authors}</p>
            <p class="mb-1 text-muted">{details_str}</p>
            <p>{links_str}</p>
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
            background-color: #1e2328;
            color: white;
            font-size: 12px;
        }}
        h2 {{
            margin-bottom: 2rem;
            color: white;
        }}
        .list-group-item {{
            background-color: transparent;
            border: none;
            color: white;
            transition: background-color 0.3s ease;
        }}
        .list-group-item:hover {{
            background-color: rgba(79, 195, 247, 0.2);
            cursor: pointer;
        }}
        .publication-title {{
            font-size: 14px; /* Tăng font size tiêu đề lên 14px */
            margin-bottom: 0.25rem;
        }}
        .text-muted {{
            color: #ccc !important;
        }}
        a {{
            color: #4fc3f7;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
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
    list_items = ""
    highlight_name = "Thanh Tuan Nguyen"
    total = len(publications)
    for idx, pub in enumerate(publications):
        display_idx = total - idx  # đánh số ngược

        title = pub.get('title', '').strip()
        authors = pub.get('authors', 'N/A').strip()
        authors = authors.replace(highlight_name, f'<strong style="color:#4fc3f7;">{highlight_name}</strong>')

        journal = pub.get('journal', '').strip()
        year = pub.get('year')
        volume = pub.get('volume', '').strip()
        issue = pub.get('issue', '').strip()
        pages = pub.get('pages', '').strip()
        doi = pub.get('doi', '').strip()
        pdf_link = pub.get('pdf_link', '').strip()

        details = []
        if journal:
            details.append(f"<em>{journal}</em>")
        if year:
            details.append(str(year))
        if volume:
            details.append(f"Vol. {volume}")
        if issue:
            details.append(f"Issue {issue}")
        if pages:
            details.append(f"pp. {pages}")
        details_str = ', '.join(details)

        links = []
        if doi:
            links.append(f'🔗 <a href="https://doi.org/{doi}" target="_blank">DOI</a>')
        if pdf_link:
            links.append(f'📄 <a href="{pdf_link}" target="_blank">PDF</a>')
        links_str = ' | '.join(links)

        list_items += f"""
        <li class="list-group-item mb-3">
            <h5 class="mb-1 publication-title">{display_idx}. {title}</h5>
            <p class="mb-1"><strong>Authors:</strong> {authors}</p>
            <p class="mb-1 text-muted">{details_str}</p>
            <p>{links_str}</p>
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
            background-color: #1e2328;
            color: white;
            font-size: 12px;
        }}
        h2 {{
            margin-bottom: 2rem;
            color: white;
        }}
        .list-group-item {{
            background-color: transparent;
            border: none;
            color: white;
            transition: background-color 0.3s ease;
        }}
        .list-group-item:hover {{
            background-color: rgba(79, 195, 247, 0.2);
            cursor: pointer;
        }}
        .publication-title {{
            font-size: 12px; /* Thu nhỏ font size tiêu đề */
            margin-bottom: 0.25rem;
        }}
        .text-muted {{
            color: #ccc !important;
        }}
        a {{
            color: #4fc3f7;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
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
    list_items = ""
    highlight_name = "Thanh Tuan Nguyen"
    total = len(publications)
    for idx, pub in enumerate(publications):
        display_idx = total - idx  # đánh số ngược

        title = pub.get('title', '').strip()
        authors = pub.get('authors', 'N/A').strip()
        authors = authors.replace(highlight_name, f'<strong style="color:#4fc3f7;">{highlight_name}</strong>')

        journal = pub.get('journal', '').strip()
        year = pub.get('year')
        volume = pub.get('volume', '').strip()
        issue = pub.get('issue', '').strip()
        pages = pub.get('pages', '').strip()
        doi = pub.get('doi', '').strip()
        pdf_link = pub.get('pdf_link', '').strip()

        details = []
        if journal:
            details.append(f"<em>{journal}</em>")
        if year:
            details.append(str(year))
        if volume:
            details.append(f"Vol. {volume}")
        if issue:
            details.append(f"Issue {issue}")
        if pages:
            details.append(f"pp. {pages}")
        details_str = ', '.join(details)

        links = []
        if doi:
            links.append(f'🔗 <a href="https://doi.org/{doi}" target="_blank">DOI</a>')
        if pdf_link:
            links.append(f'📄 <a href="{pdf_link}" target="_blank">PDF</a>')
        links_str = ' | '.join(links)

        list_items += f"""
        <li class="list-group-item mb-3">
            <h5 class="mb-1">{display_idx}. {title}</h5>
            <p class="mb-1"><strong>Authors:</strong> {authors}</p>
            <p class="mb-1 text-muted">{details_str}</p>
            <p>{links_str}</p>
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
            background-color: #1e2328;
            color: white;
            font-size: 12px;
        }}
        h2 {{
            margin-bottom: 2rem;
            color: white;
        }}
        .list-group-item {{
            background-color: transparent;
            border: none;
            color: white;
            transition: background-color 0.3s ease;
        }}
        .list-group-item:hover {{
            background-color: rgba(79, 195, 247, 0.2);
            cursor: pointer;
        }}
        .text-muted {{
            color: #ccc !important;
        }}
        a {{
            color: #4fc3f7;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
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
    csv_file = r"C:\Users\ThanhTuanNguyen\Documents\GitHub\site\publications.csv"
    publications = load_publications(csv_file)
    publications_sorted = sort_publications(publications)
    html_output = generate_html(publications_sorted)
    save_html(html_output)

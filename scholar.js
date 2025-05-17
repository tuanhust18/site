// scholar.js
document.addEventListener("DOMContentLoaded", function () {
    const container = document.getElementById("publications");
  
    fetch("https://serpapi.com/search.json?engine=google_scholar_author&author_id=V3Qc_HsAAAAJ&api_key=d83574e9881757768965d462eec78a446bd242b633b1f73378539004988be08c")
      .then(response => response.json())
      .then(data => {
        const pubs = data.articles;
        let html = "<ul>";
        pubs.forEach(p => {
          html += `<li><strong>${p.title}</strong>. <em>${p.publication}</em>, ${p.year}. <a href="${p.link}" target="_blank">Link</a></li>`;
        });
        html += "</ul>";
        container.innerHTML = html;
      })
      .catch(() => {
        container.innerHTML = "<p>Failed to load publications. Try again later.</p>";
      });
  });
  
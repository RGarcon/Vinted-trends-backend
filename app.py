import requests
from bs4 import BeautifulSoup

def scrap_vinted(query, num_pages=1):
    base_url = "https://www.vinted.fr/vetements"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    results = []

    for page in range(1, num_pages + 1):
        params = {
            "search_text": query,
            "page": page
        }

        response = requests.get(base_url, headers=headers, params=params)
        soup = BeautifulSoup(response.text, "html.parser")

        items = soup.find_all("div", class_="feed-grid__item")

        for item in items:
            try:
                title = item.find("h3").get_text(strip=True)
                price = item.find("div", class_="feed-item__price").get_text(strip=True)
                url = "https://www.vinted.fr" + item.find("a")["href"]
                results.append({"title": title, "price": price, "url": url})
            except AttributeError:
                continue  # Skip if the structure has changed

    return results

# Exemple d’utilisation
articles = scrap_vinted("nike", num_pages=2)
for article in articles:
    print(article)

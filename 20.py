import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def extract_news_links(url):

    headers = {
        "User-Agent": "Mozilla/5,0(Windows NT 10.0: Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

    }

    try:
        response  = requests.get(url,headers=headers,timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve web page: {e}")
        return []

    soup  = BeautifulSoup(response.text,"html.parser")
    news_items = []

    for a_tag in soup.find_all("a",href=True):
        headline = a_tag.get_text(strip=True)
        link = a_tag["href"]

        absolute_link = urljoin(url,link)

        if headline and len(headline) > 15 and absolute_link.startswith("http"):
            news_items.append({"headline": headline, "link": absolute_link})

    return news_items

if __name__ == "__main__":

    target_url = "http://news.ycombinator.com/"

    print(f"Extracting headlines from: {target_url}\n")
    articles = extract_news_links(target_url)

    for idx,article in enumerate(articles[:10], start=1):
        print(f"{idx}. {article['headline']}")
        print(f"  URL: {article['link']}\n")
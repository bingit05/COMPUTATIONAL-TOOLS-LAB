import csv
import requests
from bs4 import BeautifulSoup


URL = "http://books.toscrape.com/catalogue/category/books_1/index.html"


def scrape_ecommerce_data():
  headers = {
      "User-Agent": (
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
          " like Gecko) Chrome/120.0.0.0 Safari/537.36"
      )
  }

  print("Fetching data from website...")
  response = requests.get(URL, headers=headers)

  if response.status_code != 200:
    print(f"Failed to retrieve page. Status code: {response.status_code}")
    return

  soup = BeautifulSoup(response.text, "html.parser")
  products = []

  # Find all product containers on the page
  items = soup.find_all("article", class_="product_pod")

  for item in items:
    # Extract Title
    title = item.find("h3").find("a")["title"]

    # Extract Price
    price = item.find("p", class_="price_color").text.strip()

    # Extract Availability Status
    availability = item.find("p", class_="instock availability").text.strip()

    products.append(
        {"Title": title, "Price": price, "Availability": availability}
    )

  # Save data to a CSV file
  filename = "products.csv"
  with open(filename, mode="w", newline="", encoding="utf-8") as csv_file:
    fieldnames = ["Title", "Price", "Availability"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for product in products:
      writer.writerow(product)

  print(f"Successfully scraped {len(products)} products and saved to {filename}")


if __name__ == "__main__":
  scrape_ecommerce_data()
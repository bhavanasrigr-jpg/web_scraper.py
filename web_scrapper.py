
import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    with open("quotes.txt", "w", encoding="utf-8") as file:
        for quote in soup.select(".quote"):
            text = quote.select_one(".text").get_text(strip=True)
            author = quote.select_one(".author").get_text(strip=True)

            file.write(text + " — " + author + "\n\n")
            print(text, "-", author)

    print("\nQuotes saved successfully in quotes.txt!")

except requests.RequestException as error:
    print("Website connection error:", error)


import requests
from bs4 import BeautifulSoup


def scrapeWebsite(url):
    response = requests.get(url)
    response.raise_for_status()
    htmlContent = response.text
    soup = BeautifulSoup(htmlContent, 'html.parser')
    return soup


# Beispielnutzung:
if __name__ == "__main__":
    url = "https://example.com"
    websiteContent = scrapeWebsite(url)
    print(websiteContent.text)

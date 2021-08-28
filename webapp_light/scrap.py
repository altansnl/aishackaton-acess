import requests
from bs4 import BeautifulSoup, NavigableString, Tag


def scrap_articles(keyword_list):

    data = []

    keywords = "+".join(keyword_list)
    URL = "https://arxiv.org/search/?query=" + keywords + "&searchtype=all&source=header"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all("li", class_="arxiv-result")[:4]
    for result in results[:4]:
        if isinstance(result, NavigableString):
            continue
        if isinstance(result, Tag):
            title = result.find_all("p", class_='title')[0].get_text()
            url = result.find_all("a", string="pdf")[0].attrs['href']
            data.append((title, url))

    return data


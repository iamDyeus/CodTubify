#scratch title from youtube URL

def get_title(url):
    import requests
    from bs4 import BeautifulSoup
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find('title')
    return title.text.removesuffix(' - YouTube')




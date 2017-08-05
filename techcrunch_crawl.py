# techcrunch popular news


def crawling_techcrunch():
    import requests
    from bs4 import BeautifulSoup as bsoup

    html = requests.get('https://techcrunch.com/popular/').text
    soup = bsoup(html, 'html.parser')
    n = 0
    D = {}
    for tag in soup.select('.post-title a'):
        D[tag.text] = tag['href']
        n += 1
        if n == 6:
            break
    return D

if __name__ == "__main__":

    crawling_techcrunch()

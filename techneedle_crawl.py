# techcrunch popular news


def crawling_techneedle():
    import requests
    from bs4 import BeautifulSoup as bsoup

    html = requests.get('http://techneedle.com').text
    soup = bsoup(html, 'html.parser')
    n = 0
    D = {}
    for tag in soup.select('.entry-title a'):
        D[tag.text] = tag['href']
        n += 1
        if n == 5:
            break
    return D

if __name__ == "__main__":

    crawling_techneedle()

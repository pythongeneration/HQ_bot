# techcmeme 5 news


def crawling_techmeme():
    import requests
    from bs4 import BeautifulSoup as bsoup

    html = requests.get('http://www.techmeme.com/').text
    soup = bsoup(html, 'html.parser')
    n = 0
    D = {}
    for tag in soup.select('#topcol1 .ii .ourh'):
        D[tag.text] = tag['href']
        n += 1
        if n == 5:
            break
    return D

if __name__ == "__main__":

    crawling_techmeme()

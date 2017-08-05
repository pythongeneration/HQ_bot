# 다음 IT 댓글 많은 뉴스


def crawling_daum():

    import requests

    from bs4 import BeautifulSoup as bsoup

    html = requests.get('http://media.daum.net/digital/').text

    soup = bsoup(html, 'html.parser')

    # print(soup)
    D = {}
    for i, tag in enumerate(soup.select('.list_popcmt a')):
        i += 1
        tag_noline = tag.text.split()
        n_tag = " ".join(tag_noline)
        D[n_tag] = tag['href']
    return print(D)


if __name__ == "__main__":

    crawling_daum()

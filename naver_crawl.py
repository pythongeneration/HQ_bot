#네이버 가장 많이 본 뉴스

def crawling_naver():

    import requests

    from bs4 import BeautifulSoup as bsoup

    html = requests.get('http://news.naver.com').text

    soup = bsoup(html, 'html.parser')

    # print(soup)
    D = {}
    for i, tag in enumerate(soup.select('#ranking_105 a')):
        i += 1
        tag_noline = tag.text.split()
        tag_html = 'http://news.naver.com' + tag['href']
        # print(i,  tag['title']+tag_html)
        D[tag['title']] = tag_html
    return print(D)


if __name__ == "__main__":

    crawling_naver()

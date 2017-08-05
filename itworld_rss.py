#itworld사이트 Rss parser

import feedparser

def RSS_parser():
    
    d = feedparser.parse('http://www.itworld.co.kr/rss/feed/')
    t = 'title'
    e = 'entries'
    l = 'link'
    n = 0
    D = {}
    for i in d:
        # print(d[e][n][t], d[e][n][l])
        D[d[e][n][t]] = d[e][n][l]
        n += 1
    return D

if __name__ == "__main__":
    RSS_parser()

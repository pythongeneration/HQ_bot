#itworld사이트 Rss parser

import feedparser

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
print(D)

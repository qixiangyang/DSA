from Excellent_Cases.sogou_spider.sgwc import search_officials

officials = search_officials(keyword='阿尔法工场')

for official in officials:

    print(official['url'])
# print(officials['url'])


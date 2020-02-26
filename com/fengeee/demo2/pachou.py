import re
import time
import requests
import pandas as pd
from retrying import retry
from concurrent.futures import ThreadPoolExecutor

start = time.clock()

plist = []
for i in range(1, 101):
    j = 44 * (i - 1)
    plist.append(j)

listno = plist
datatmsp = pd.DataFrame(columns=[])

while True:
    @retry(stop_max_attempt_number=8)
    def network_programming(num):
        url = 'https://s.taobao.com/search?q=%E6%B2%99%E5%8F%91&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=0&ntoffset=6&p4ppushleft=' \
              '%2C44&sort=sale-desc&filter=reserve_price%5B500%2C%5D&s=' + str(num)
        web = requests.get(url, headers=headers)
        web.encoding = 'utf-8'
        return web


    def multithreading():
        number = listno
        event = []

        with ThreadPoolExecutor(max_workers=10) as executor:
            for result in executor.map(network_programming, number, chunksize=10):
                event.append(result)
        return event


    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}

    listpg = []
    event = multithreading()
    for i in event:
        json = re.findall('"auctions":(.*?),"recommendAuctions"', i.text)
        if len(json):
            table = pd.read_json(json[0])
            datatmsp = pd.concat([datatmsp, table], axis=0, ignore_index=True)
            pg = re.findall('"pageNum":(.*?),"p4pbottom_up"', i.text)[0]
            listpg.append(pg)

    lists = []
    for a in listpg:
        b = 44 * (int(a) - 1)
        lists.append(b)

    listn = listno

    listno = []

    for p in listn:
        if p not in lists:
            listno.append(p)

    if len(listno) == 0:
        break

datatmsp.to_excel('datatmsp.xls', index=False)

end = time.clock()
print("爬取完成，用时:", end - start, 's')

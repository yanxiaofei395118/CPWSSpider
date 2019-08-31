import time

import requests
import json
from lxml import etree
import re
import traceback

"""
爬取全国所有法院名称用于裁判文书搜索
"""


def get_proxy():
    # 获取代理ip方法请自行封装
    # 免费代理ip爬取: https://github.com/SelemeneCFY/ip_pool.git
    pass


start_url = "http://tingshen.court.gov.cn/court"
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}


def main():
    resp = requests.get(start_url, headers=headers, proxies=get_proxy())
    tree = etree.HTML(resp.content)
    print(resp.text)
    code_li = tree.xpath("//div[@class='region-city _region_city']/span/@areacode")
    print(len(code_li))
    name_li = []
    for code in code_li:
        p_url = start_url + '?areaCode=' + code
        r = requests.get(p_url, headers=headers, proxies=get_proxy())
        time.sleep(1)
        tree = etree.HTML(r.content)
        fy_name = tree.xpath("//a[contains(@href,'/court/')]//text()")
        name_li += fy_name
    name_li = list(set(name_li))
    # print(len(name_li))
    with open('fymc.txt', 'a')as f:
        for name in name_li:
            f.write(name + '\r\n')


if __name__ == '__main__':
    # print(get_proxy())
    main()

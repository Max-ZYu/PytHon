# !usr/bin/evn python
# -*-  coding:utf-8  -*-
# by ：张瑜ing

import requests
from bs4 import BeautifulSoup

def get_td():
    elemt = element.select('table td')  # ('table td')为CSS选择器，选择table标签下所有的td元素
    with open('tg_hn.html', 'a+', encoding='gb2312') as f:
        for line in elemt[4:8]:  # elemt[4:8] 为表头标题部分的代码
            line = str(line)
            f.write(line + '\n')

def get_table():
    elem = element.select('#gvGridView')  # elem 为名单部分的纯净代码，结果是list，其中元素为Tag类型。
    with open('tg_hn.html', 'a+', encoding='gb2312') as f:
        for line in elem:
            line = str(line)
            f.write(line + '\n')
        fgf = '~' * 30
        f.write('<p>' + fgf + '</p>')

quxian = [410122,410221,410222,410223,410224,410225,410322,410323,410324,410325,410326,410327,410328,410329,410421,410422,410423,410425,410522,410523,410526,410527,410621,410622,410721,410724,410725,410726,410727,410728,410821,410822,410823,410825,410922,410923,410926,410927,410928,411023,411024,411025,411121,411122,411221,411222,411224,411321,411322,411323,411324,411325,411326,411327,411328,411329,411330,411421,411422,411423,411424,411425,411426,411521,411522,411523,411524,411525,411526,411527,411528,411621,411622,411623,411624,411625,411626,411627,411628,411721,411722,411723,411724,411725,411726,411727,411728,411729 ]  # a。9个县
xueke = list(range(11, 25))  # k。14个学科
xueduan = [1, 2]  # s。1为小学，2为中学
i = 0

if __name__ == '__main__':
    for a in quxian:
        for k in xueke:
            for s in xueduan:
                i = i + 1
                url = 'http://tgzp.haedu.cn/msgg.aspx?a=' + str(a) + '&k=' + str(k) + '&s=' + str(s)

                r = requests.get(url)  # 模拟访问网页
                print(str(r) + '--------访问成功' + str(i) + '次')
                url_text = r.content.decode("gb2312", errors='ignore')  # <class 'str'>
                content = BeautifulSoup(url_text, features="lxml")  # 获得网页源代码.<class 'bs4.BeautifulSoup'>
                element = content.find('table')  # element 为表部分的所有代码. <class 'bs4.element.Tag'>

                get_td()
                get_table()

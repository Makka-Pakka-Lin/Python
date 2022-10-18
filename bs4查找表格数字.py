import requests
from bs4 import BeautifulSoup
import re


class Solution:

    def table_num(self,
                  row: int,
                  col: int) -> int:
        curentRow = -1
        x = -1
        url = "http://72.itmc.org.cn/JS001/open/show/random-num/index.html"
        resp = requests.get(url)
        page = BeautifulSoup(resp.text, "html.parser")
        for table in page.findAll('table'):  # 查找所有表格
            for row_N in table.findAll('tr'):
                curentRow += 1
                if curentRow == row:
                    for tr in row_N.findAll('td'):  # 查找表格肉容
                        x += 1
                        if x == col:
                            aaa = row_N.select('td')[col].text
                            print(int(aaa))
            break
        return aaa
        pass


a = Solution()
row = int(input("第几行"))
col = int(input("第几列"))
a.table_num(row, col)

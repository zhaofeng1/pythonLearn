'''
Created on 2017年1月3日
测试 抓取
需要安装模块  ：bs4(beautifulSoup4),
@author: Administrator
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
from learn.crawler.ProdInfo import ProdInfo
class Spider:
    
    def __init__(self):
        self.siteUrl = "http://www.lazada.co.id/catalog/?q="
        
    def getSearchResult(self,search):
        url = self.siteUrl + str(search)
        print(url)
        try:
            doc = urlopen(url, None, 60*1000).read()
            pList = self.get_product_a(doc)
            print(pList)
            for purl in pList:
                self.get_product_info(purl)
            
        except ValueError as e:
            print("ValueError :{0}".format(e))
            
    #获取商品的前5个连接
    def get_product_a(self,doc):
        "获取商品的前5个连接"
#         path = "E:/crawler/pythontxt.html"
#         # 打开文件
#         try:
#             f = open(path, "r",encoding= 'utf-8')
#             for line in f.readlines():
#                 doc = doc+line
#         except ValueError as e:
#             print("ValueError :{0}".format(e))
#         
#         print("=======")
        
        pList = []
        if len(doc)>1:
            soup = BeautifulSoup(doc)
            productDiv = soup.select('div[data-component="product_list"]')[0]
            alla = productDiv.find_all("a",limit=5)
            for a in alla:
                print(a.get('href'))
                pList.append(a.get('href'))
            print(pList)
        return pList
    
    #根据商品连接获取商品信息
    def get_product_info(self,url):
        prodInfo = ProdInfo()
        try:
            doc = urlopen(url, None, 60*1000).read()
            if(len(doc)):
                soup = BeautifulSoup(doc)
                self.get_title(soup)
            
        except ValueError as e:
            print("ValueError :{0}".format(e)) 
    def get_title(self,soup):
        titleTag = soup.find_all(id='prod_title')[0]
        print(titleTag.string.strip())
        
    def has_class(self,tag):
        return tag.has_attr('data-sku-simple')
     
        
spider = Spider()
spider.getSearchResult("Jam")


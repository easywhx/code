import requests
import json
from lxml import etree
class qiubaisplider:
    def __init__(self):
      self.url_temp = "https://www.qiushibaike.com/8hr/page/{}/"
      self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}

    def get_url_list(self):
         url_list = [self.url_temp.format(i) for i in range(1,14)]
         return url_list;

    def parse_url(self,url):
        response = requests.get(url,headers = self.headers)
        response.encoding="utf-8"
        return response.text


    def get_content_list(self,html_url):
         html = etree.HTML(html_url)
         print("---------------------------------------------------")
         print(html)
        #分组
         li_list = html.xpath("//div[@class='recommend-article']/ul/li[@class='item typs_video']")
         print(li_list)
         content_list=[]
         for li in li_list:
           item = {}
           item["vedio"] = li.xpath("./a/@href")[0]
           item["title"] = li.xpath("./div[@class='recmd-right']/a/text()")[0]
           item["author_image"]=li.xpath("./div[@class='recmd-right']//a/img/@src")
           item["author_image"]="https:"+item["author_image"][0]
           item["author_name"]=li.xpath("./div[@class='recmd-right']//a/span/text()")[0]
           item["smile_num"]=li.xpath("./div[@class='recmd-right']/div/div/span/text()")[0]
           item["recmd_num"] = li.xpath("./div[@class='recmd-right']/div/div/span/text()")[3]
           content_list.append(item)
           print(item)
         return content_list



    def save_content_list(self,content_list):
        with open("qiushi.txt","a",encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content,ensure_ascii=False))
                f.write("\n")
        print("保存成功")

    def run(self):
        url_list = self.get_url_list()
        print(url_list)
        for url in url_list:
            html_str = self.parse_url(url)
            content_list = self.get_content_list(html_str)
            self.save_content_list(content_list)

if __name__=="__main__":
    qiubaisplider = qiubaisplider()
    qiubaisplider.run()

import json
from parse import parse_url




class Douban_splider:

    temple_url = "https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?os=android&for_mobile=1&start={}&count=18&loc_id=108288&_=0"

    def get_content_list(self,json_html):
        dic_data = json.loads(json_html)
        content_list = dic_data["subject_collection_items"]
        total = dic_data["total"]
        return content_list,total

    def save_content_list(self,content_list):
        with open("do.json","a",encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content,ensure_ascii=False))
                f.write("\n")

        print("save success")
    def run(self):#实现的主要逻辑
        num = 0;
        total = 10;
        while(num<total):#循环请求
            #开始的url
            start_url = self.temple_url.format(num)
            #发送网络请求
            json_str=parse_url(start_url)
            #提取数据
            content_list,total = self.get_content_list(json_str)
            # 保存数据
            self.save_content_list(content_list)
            #构造下一页的URL地址，循环以上步骤
            num+=18

if __name__=='__main__':
     douban_spliser = Douban_splider();
     douban_spliser.run()
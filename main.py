import feedparser
import time
import os
import re
import pytz
from datetime import datetime

def get_link_info(feed_url, num):

    result = ""
    feed = feedparser.parse(feed_url)
    feed_entries = feed["entries"]
    feed_entries_length = len(feed_entries)
    all_number = 0;

    if(num > feed_entries_length):
        all_number = feed_entries_length
    else:
        all_number = num
    
    for entrie in feed_entries[0: all_number]:
        title = entrie["title"]
        link = entrie["link"]
        result = result + "\n" + "[" + title + "](" + link + ")" + "\n"
    
    return result
    








def main():


    
    RuisiHe_info =  get_link_info("https://ruisihe.github.io/notes/", 3)
    print(RuisiHe_info)
  

    insert_info =  RuisiHe_info

    # 替换 ---start--- 到 ---end--- 之间的内容
    # pytz.timezone('Asia/Shanghai')).strftime('%Y年%m月%d日%H时M分')
    fmt = '%Y-%m-%d %H:%M:%S %Z%z'
    insert_info = "---start---\n\n## 最近更新文章(" + "更新时间:"+  datetime.fromtimestamp(int(time.time()),pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S') + " | 通过Github Actions自动更新)" +"\n" + insert_info + "\n---end---"
    # 获取README.md内容
    with open (os.path.join(os.getcwd(), "README.md"), 'r', encoding='utf-8') as f:
        readme_md_content = f.read()

    print(insert_info)

    new_readme_md_content = re.sub(r'---start---(.|\n)*---end---', insert_info, readme_md_content)

    with open (os.path.join(os.getcwd(), "README.md"), 'w', encoding='utf-8') as f:
        f.write(new_readme_md_content)



main()

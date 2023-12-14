import requests
from bs4 import BeautifulSoup
import os

base_url = "https://www.ndrc.gov.cn/xwdt/ztzl/gncpyjg/"
root = "C://Users//Lenovo//Desktop//网页"

page_urls = []
#处理第一页
url = f"{base_url}index.html"
print(url)
response = requests.get(url)
content = response.text
soup = BeautifulSoup(content, "html.parser")
links = soup.find_all('a')  # 找到每一页的URL链接
for link in links:
    ur = link.get('href')
    if len(ur) < 31:
        continue
    else:
        ur = ur[2:]
        page_urls.append(ur)  # 将URL添加到列表中

#处理2~10页
for page in range(1, 10):
    url = f"{base_url}index_{page}.html"
    print(url)
    response = requests.get(url)
    content = response.text
    soup = BeautifulSoup(content, "html.parser")
    links = soup.find_all('a')  # 找到每一页的URL链接
    for link in links:
        ur = link.get('href')
        if len(ur) < 31:
            continue
        else:
            ur = ur[2:]
            page_urls.append(ur)  # 将URL添加到列表中


image_urls = []
for i in page_urls:
    url = f"{base_url}{i}"
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, "html.parser",from_encoding='utf-8')
    container = soup.find('div', {'class': 'container'})
    #print(container)
    try:
        trs_editor = container.find('div', {'class': 'TRS_Editor'})
        for img in trs_editor.find_all('img'):
            print(url[:48]+img.get('src')[1:])
            image_urls.append(url[:48]+img.get('src')[1:])
    except:
        print("本网页没有图片")


# 保存图片
for i, link in enumerate(image_urls):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            # 提取图片文件名
            file_name = link.split('/')[-2]+link.split('/')[-1]
            file_path = os.path.join(root, file_name)

            # 保存图片
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f"第{i+1}张图片保存成功")
        else:
            print(f"第{i+1}张图片下载失败")
    except Exception as e:
        print(f"第{i+1}张图片下载出错：{str(e)}")
    




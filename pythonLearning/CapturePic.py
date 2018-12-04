import requests
import urllib.request
from bs4 import BeautifulSoup
import os
import time

url = 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2537158013.jpg'
folder_path = './pic/'

html = requests.get(url)
image = folder_path + 'test' +'.png'

if os.path.exists(folder_path) == False:  # 判断文件夹是否已经存在
    os.makedirs(folder_path)  # 创建文件夹
    
with open(image, 'wb') as file:
    file.write(html.content)
    file.flush()
    file.close()

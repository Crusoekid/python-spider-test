from bs4 import BeautifulSoup
import requests
import os

url = 'https://book.douban.com/'
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')
file_name = 'links.txt'
path = './linkFolder/'
isClazzTag = False
href = ''

if os.path.exists(path) == False:
    os.makedirs(path)

for link in soup.find_all('a'):
    if link:
        isClazzTag = False
        clazz = link.get('class')
        if clazz != None:
            for i in clazz:
                if i == 'tag':
                    isClazzTag = True
                    break
        if isClazzTag:
            href = url + link.get('href')
        else:
            href = link.get('href')         
        print(href)
        if os.path.exists(file_name + path):
            with open(path + file_name, 'w') as file:
                if href:
                    file.write(href + '\n')
        else:
            with open(path + file_name, 'a') as file:
                    if href:
                        file.write(href + '\n') 


    

# print(soup.get_text())

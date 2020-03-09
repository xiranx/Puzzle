import requests
import urllib.request
from bs4 import BeautifulSoup
import os
import time

url = "https://www.google.com/search?rls=en&q=%E4%B8%9C%E6%96%B9%E7%A5%9E%E8%B5%B7%E5%9B%BE%E7%89%87%E5%BA%93&tbm=isch&source=univ&client=safari&sa=X&ved=2ahUKEwje_Pa52OHnAhU0muYKHTI8BhMQsAR6BAgKEAE&biw=1336&bih=688"
headers = {'User-Agent':'Mozilla/5.0'}
response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.content,'html.parser')
items = soup.find_all('img')
folder_path = '/Users/xxr/Desktop/TVXQ_photo/'
if os.path.exists(folder_path) ==False:
    os.makedirs(folder_path)


print(items)
print(len(items))
for index,item in enumerate(items):
    if item:
        try:
            html = requests.get(item.get('src'))
            img_name = folder_path+str(index+1)+'.png'
            with open(img_name,'wb') as file:
                file.write(html.content)
                file.flush()
                file.close()
                print('第%d张图片下载完成' %(index+1))
                time.sleep(1)
        except:
            print('no src or no url')
print('抓取完成')


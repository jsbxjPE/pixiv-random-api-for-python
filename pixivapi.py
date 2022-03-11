from dataclasses import dataclass
import requests
import json

#初始化
global data
global original_url
global id_url
global jpg_url
global name_url
global num_x
global num_m
global num_c
data = []
original_url = []
id_url = []
jpg_url = []
name_url = []
num_x = 1
num_m = 1
num_c = 1

def search(r18, num): #api搜索图片
    global data
    global original_url
    global id_url
    global jpg_url
    global name_url
    global num_x
    global num_m
    global num_c
    data = []
    original_url = []
    id_url = []
    jpg_url = []
    name_url = []
    num_x = 1
    num_m = 1
    num_c = 1
    if num > 100:
        num_y = num % 100
        while num_x:
            if (num - num_y) / num_m == 100:
                num_x = 0
            else:
                num_m = num_m + 1
        for i in range(num_m):
            data = json.loads(requests.get(url = 'https://api.lolicon.app/setu/v2?r18={}&num=100'.format(str(r18))).text)['data']
            for i in range(len(data)):
                original_url.append(data[i]['urls']['original'])
                name_url.append(data[i]['title'])
            for i in original_url:
                id_url.append(i.split('/')[11].split('_')[0])
            for i in id_url:
                jpg_url.append('https://pximg.rainchan.win/img?img_id={}'.format(i))
        for i in range(num_y):
            data = json.loads(requests.get(url = 'https://api.lolicon.app/setu/v2?r18={}&num={}'.format(str(r18), str(num))).text)['data']
            for i in range(len(data)):
                original_url.append(data[i]['urls']['original'])
                name_url.append(data[i]['title'])
            for i in original_url:
                id_url.append(i.split('/')[11].split('_')[0])
            for i in id_url:
                jpg_url.append('https://pximg.rainchan.win/img?img_id={}'.format(i))
    else:
        for i in range(num):
            data = json.loads(requests.get(url = 'https://api.lolicon.app/setu/v2?r18={}&num={}'.format(str(r18), str(num))).text)['data']
            for i in range(len(data)):
                original_url.append(data[i]['urls']['original'])
                name_url.append(data[i]['title'])
            for i in original_url:
                id_url.append(i.split('/')[11].split('_')[0])
            for i in id_url:
                jpg_url.append('https://pximg.rainchan.win/img?img_id={}'.format(i))

def download(path): #切换api下载图片
    global jpg_url
    for i in range(len(jpg_url)):
        content = requests.get(url=jpg_url[i]).content
        name = '{}/{}.jpg'.format(path, name_url[i])
        with open(name, 'wb') as f:
            f.write(content)

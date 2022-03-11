# pixiv-api-for-python
 pixiv-api-for-python

## 前言

### 本人第一次做,代码如果有BUG请原谅

## 依赖

```sh
pip install requests
```

## 快速开始

导入库文件

```python
import pixivapi
```

搜索

```python
pixivapi.search(r18 = '1', num = number)
```

下载

```python
pixivapi.download(path = 'your path')
```

## 使用方法

### pixivapi.search

* num {Int} 爬取图片数量
* r18 {Srting} 要r18输入1，不要r18输入0，混合输入2

### wallhavenapi.download

* path {Srting} 下载文件夹路径
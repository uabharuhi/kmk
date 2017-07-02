# uncompyle6 version 2.11.1
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.6.1 |Anaconda 4.4.0 (64-bit)| (default, May 11 2017, 13:09:58) 
# [GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]
# Embedded file name: /home/uabharuhi/python/dl/kumiko/crawler.py
# Compiled at: 2017-07-02 15:57:44
# Size of source mod 2**32: 2184 bytes
import scrapy

class ImageSpider(scrapy.Spider):
    name = 'Kumiko spider'
    MAX_IMAGE_NUM = 50

    def start_requests(self):
        print('start request')
        names = [
         'yome',
         'reina',
         'other']
        urls = [
         'https://www.google.com.tw/search?q=kumiko+hibike+euphonium&tbm=isch',
         'https://www.google.com.tw/search?q=kumiko+hibike+euphonium&tbm=isch',
         'https://www.google.com.tw/search?q=anime&tbm=isch']
        for i, url in enumerate(urls):
            character_name = names[i]
            request = scrapy.Request(url=url,callback=self.parse,)
            request.meta['character_name'] = character_name
            request.meta['request_cnt'] = 0
            yield request
            break

    def parse(self, response):
        print('parse')
        cnt = response.meta['request_cnt']
        img_urls = response.css('img::attr(src)').extract()
        print('img ulrs')
        for img_url in img_urls:
            if cnt > self.MAX_IMAGE_NUM:
                break
            print(img_url)
            request = scrapy.Request(url=img_url,callback=self.parseImages,)
            request.meta['character_name'] = response.meta['character_name']
            request.meta['request_cnt'] = cnt
            yield request
            cnt += 1

        if cnt < self.MAX_IMAGE_NUM:
            next_page_url = response.css('td.b a.fl::attr(href)').extract_first()
            if next_page_url is None:
                print('next page is None')
            else:
                request = response.follow(url=next_page_url,callback=self.parse,)
                request.meta['character_name'] = response.meta['character_name']
                request.meta['request_cnt'] = cnt
                yield request

    def parseImages(self, response):
        print('parseImages')
        print(response.url)
        dirname = './image/%s' % response.meta['character_name']
        img_filename = '%s/%s' % (dirname, response.meta['request_cnt'])
        with open(img_filename, 'wb') as f:
            print(img_filename)
            f.write(response.body)
        self.log('Saved file %s' % img_filename)
# okay decompiling ./crawler.cpython-36.pyc


#https://stackoverflow.com/questions/22648475/understanding-callbacks-in-scrapy
import scrapy

class ImageSpider(scrapy.Spider):
    name = 'Kumiko spider'
    MAX_IMAGE_NUM = 50
    #thread lock?
    character_img_cnt={}

    def start_requests(self):
        print('start request')
        names = [
         'yome',
         'reina',
         'other']
        urls = [
         'https://www.google.com.tw/search?q=kumiko+hibike+euphonium&tbm=isch',
         'https://www.google.com.tw/search?q=reina+hibike+euphonium&tbm=isch',
         'https://www.google.com.tw/search?q=anime&tbm=isch']
        for i, url in enumerate(urls):
            character_name = names[i]
            request = scrapy.Request(url=url,callback=self.parse)
            request.meta['character_name'] = character_name
            yield request
            

    def parse(self, response):
        print('parse')
        character_name = response.meta['character_name']

        if character_name  not in self.character_img_cnt:
            self.character_img_cnt[character_name] = 0

        img_urls = response.css('img::attr(src)').extract()
        print('img ulrs')
        for img_url in img_urls:
            #no lock so will get different images number
            if self.character_img_cnt[character_name] > self.MAX_IMAGE_NUM:
                break
            print(img_url)
            request = scrapy.Request(url=img_url,callback=self.parseImages)
            request.meta['character_name'] = response.meta['character_name']
           
            yield request
            

        if  self.character_img_cnt[character_name] < self.MAX_IMAGE_NUM:
            ##next page , prev page  back go....loop duplicate
            # prev and next both has the same selector
            #next_page_url = response.css('td.b a.fl::attr(href)').extract_first()
            next_page_url = response.css('td.b a.fl::attr(href)').extract()[-1]
            if next_page_url is None:
                print('next page is None')
            else:
                #print('re:')
                #print(next_page_url)
                request = response.follow(url=next_page_url,callback=self.parse,)
                request.meta['character_name'] = response.meta['character_name']
               
                yield request

    def parseImages(self, response):
        #if > number of max... --> dont do that becuase can get more images
        print('parseImages')
        print(response.url)
        character_name = response.meta['character_name']
        dirname = './image/%s' %(character_name)
        img_filename = '%s/%s' % (dirname,self.character_img_cnt[character_name])
        with open(img_filename, 'wb') as f:
            print(img_filename)
            f.write(response.body)
            self.character_img_cnt[character_name]+=1
        print('Saved file %s' % img_filename)


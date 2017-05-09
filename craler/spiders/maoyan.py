#encoding: utf-8
import re
import requests
import time
from bs4 import BeautifulSoup
import scrapy
from scrapy.http import Request
from craler.items import CralerItem
import urllib2
from scrapy.spiders import CrawlSpider, Rule

from craler.pipelines import CralerPipeline



class MoyanSpider(CrawlSpider):
    try:
        name = 'maoyan'
        allowed_domains = ["http://maoyan.com"]

    except Exception, e:
        print e.message

    def start_requests(self):
        for i in range(22863):
            url = ("http://maoyan.com/films?offset=%s" % str(i*30))

            yield Request(url,self.parse)

    def parse(self, response):
        try:
            time.sleep(10)

            # if CralerPipeline.check(response.url):
            #    
            #    pass
            # 
            # else:

            headers = {}
            headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36"
            item = CralerItem()

            movies = BeautifulSoup(response.text, 'lxml').find("div", class_="movies-list").find_all("dd")
            for movie in movies:
                time.sleep(2)
                item['name'] = movie.find("div", class_="channel-detail movie-item-title").get_text()
                item['score'] = movie.find("div", class_="channel-detail channel-detail-orange").get_text()
                url = "http://maoyan.com" + movie.find("div", class_="channel-detail movie-item-title").find("a")[
                    "href"]
                # item['url'] = url
                item['id'] = url.split("/")[-1]
                html = requests.get(url).content
                soup = BeautifulSoup(html, 'lxml')
                temp = soup.find("div", "movie-brief-container").find("ul").get_text()
                temp = temp.split('\n')
                # item['cover'] = soup.find("div","avater-shadow").find("img")["src"]
                item['tags'] = temp[1]
                item['countries'] = temp[3].strip()
                item['duration'] = temp[4].split('/')[-1]
                item['time'] = temp[6]

                yield item
                
        except Exception, e:
            print e.message


                

            

#-*- coding: utf-8 -*-

'''
from scrapy.selector import Selector
from scrapy import Spider
from scrapySpyder.items import Article

# simply collecting the title field from each page

class ArticleSpider(Spider):
    name = 'article'
    allow_domains = ['en.wikipedia.org']
    start_urls = ['http://en.wikipedia.org/wiki/Main_Page', 'http://en.wikipedia.org/wiki/Python_%28programming_language%29']

    def parse(self, response):
        item = Article()
        title = response.xpath('//h1/text()')[0].extract()
        print('Title is: ' + title)
        item['title'] = title
        return item
'''
# --------------------------------------------------------------------------------------
'''
turn it into a fully fledged crawler, you
need to define a set of rules that Scrapy can use to seek out new URLs on each page it
encounters:
'''
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapySpyder.items import Article
from scrapy.linkextractors import LinkExtractor

# packge below would output a ImportError: no module named 'sgmllib', this module removed by py3.x, replace it with linkextractors
# from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

class ArticleSpider(CrawlSpider):
    name = 'article'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['http://en.wikipedia.org/wiki/Python_%28programming_language%29']
    rules = [Rule(LinkExtractor(allow=('(/wiki/)((?!:).)*$'),), callback='parse_item', follow=True)]

    def parse(self, response):
        item = Article()
        title = response.xpath('//h1/text()')[0].extract()
        print('Title is: ' + title)
        item['title'] = title
        return item
import scrapy
from scrapy import Selector
from UnivList import items
#from scrapy.contrib.spiders import CrawlSpider, Rule
#from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor

class UnivListSpider(scrapy.Spider):
	name = "univ_list"
	allowed_domains = ["univ.cc"]
	#Change start url for different countries....
	start_urls = [
		'http://univ.cc/search.php?dom=edu_tx&key=&start=1',
		'http://univ.cc/search.php?dom=edu_tx&key=&start=51'
	]
	'''
	rules = (Rule(LxmlLinkExtractor(allow=("search.php?dom=[a-z]{2}.*?key=.*?start=\d{2,}", ),
			restrict_xpaths=('//nav[@class="resultNavigation"]',))
			, callback="parse", follow= True),
	)
	
	rules = (Rule(LxmlLinkExtractor(allow=(),
			restrict_xpaths=('//nav[@class="resultNavigation"]',))
			, callback="parse_items", follow= True),
	)'''
	
	def parse(self, response):
		hxs = Selector(response)
		urls = hxs.xpath("//li")
		unv_list = []
		for url in urls:
			item = items.UnivlistItem()
			item ["title"] = url.select("a/text()").extract()
			item ["link"] = url.select("a/@href").extract()
			unv_list.append(item)
		return unv_list

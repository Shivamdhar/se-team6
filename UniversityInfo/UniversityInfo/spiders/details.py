import urlparse
import scrapy
from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import Selector
from UniversityInfo import items

class DetailsSpider(CrawlSpider):
	handle_httpstatus_list = [403]
	
	name = "details"
	allowed_domains = ["usnews.com"]
	start_urls = (
		'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities',
		'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/page+2',
		'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/page+3',
		'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/page+4',
		'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/page+5',
		'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/page+6',
		'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/page+7',
		'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/page+8',
		'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/page+9',
		'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/page+10',
		'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/page+11',
		'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/page+12',
		'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/page+13',
		'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/page+14',
		'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/page+15',
		'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/page+16',
		'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/page+17',
		'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/page+18',
		'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/page+19',
		'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/page+20',
		'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/page+21',
		'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/page+22',
		'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/page+23',
		'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/page+24',
		'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/page+25'
	)

	def parse(self, response):
		school_info = response.selector.xpath("//div[@class='school-info']")
		school_image = response.selector.xpath("//div[@class='school-image']")
		ranks = response.selector.xpath("//span[@class='rankscore-bronze cluetip cluetip-stylized']")
		#p_desc = response.selector.xpath("//p")
		univ_details = []

		#for sch_info, sch_img, rank, p in zip(school_info,school_image,ranks,p_desc):
		for sch_info, sch_img, rank in zip(school_info,school_image,ranks):
			item = items.UniversityinfoItem()
			
			item ["name"] = sch_info.xpath("h2[@class='h h-flush h-cramped']/a[@class='school-name']/text()").extract()
			item ["link"] = sch_info.xpath("h2[@class='h h-flush h-cramped']/a[@class='school-name']/@href").extract()
			item ["location"] = sch_info.xpath("p[@class='t t-smaller t-subdued']/text()").extract()
						
			item ["image_urls"] = sch_img.xpath("a/img/@src").extract()
			absolute_url = urlparse.urljoin(response.url, item ["image_urls"][0].strip())
			item ["image_urls"] = [absolute_url] 

			stat = sch_img.xpath("dl[@class='stat']/dd/text()").extract()
			stat_dt = sch_img.xpath("dl[@class='stat']/dt/text()").extract()

			if stat_dt[0] == "In-state tuition and fees:":
				item ["tuitionFee"] = "In-state: " + stat[0] + " Out-state: " + stat[1]
				if stat_dt[2] == "Enrollment:":			 
					item ["enrollment"] = stat[2]
					#item ["settings"] = stat[3]
				else:
					item ["enrollment"] = ""

			elif stat_dt[0] == "Tuition and fees:":
				item ["tuitionFee"] = stat[0]
				if stat_dt[1] == "Enrollment:":
					item ["enrollment"] = stat[1]
					#item ["settings"] = stat[2]
				else:
					item ["enrollment"] = ""

			elif stat_dt[0] == "Enrollment:":
				item ["enrollment"] = stat[0]
				item ["tuitionFee"] = ""

			rank = rank.xpath("./text()").extract()
			item ["rank"] = rank if rank else "Unranked"
			#item ["desc"] = p.xpath("./text()").extract()
			univ_details.append(item)
		return univ_details

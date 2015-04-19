# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import Selector
from scholarshipInd import items

class ScholarshipIndSpider(CrawlSpider):
	name = "scholarship_ind"
	allowed_domains = ["http://www.topuniversities.com"]
	start_urls = (
		'http://www.topuniversities.com/student-info/scholarship-advice/international-scholarships-indian-students',
	)

	def parse(self, response):
		strng_a = response.selector.xpath("//strong/a")
		a_strng = response.selector.xpath("//a[contains(.,'ship')]")
		scholarship_info = []
		
		for x in strng_a:
			sa = items.ScholarshipindItem()
			sa['title'] = x.xpath("./text()").extract() 
			sa['link'] = x.xpath("@href").extract()
			scholarship_info.append(sa)

		del scholarship_info[-1]
		
		for y in a_strng:			
			ast = items.ScholarshipindItem()
			title = y.xpath('strong/text()').extract()

			if title:
				ast['title'] = title
				ast['link'] = y.xpath('@href').extract()
				scholarship_info.append(ast)

		return scholarship_info
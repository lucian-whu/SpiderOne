# -*- coding: utf-8 -*-
import re

from scrapy.spiders import CrawlSpider, Request

from SpiderOne.items import SpideroneItem


class TestoneSpider(CrawlSpider):
    name = "testone"
    # allowed_domains = ["http://journals.plos.org/plosone/"]

    count = 1  # article count
    start_urls = ['http://journals.plos.org/plosone/browse/']

    def parse_start_url(self, response):
        # call parse_page for start url
        print(response.url + "这是response.url的内容")
        yield Request(response.url, callback=self.parse_page)

    def parse_page(self, response):
        # grab article url
        urls = response.xpath('//div[@class="article-block"]//a[@class="article-url"]/@href').extract()

        # add domain to url and call parse_item on each article url
        for url in urls:
            url = 'http://journals.plos.org' + url
            yield Request(url, callback=self.parse_item)

            # grab link for the next page
            next_page = response.xpath('//nav[@class="nav-pagination"]//a[@id="nextPageLink"]/@href').extract()

            # if there is a next page, follow the link and call parse_page on it
            if len(next_page) is not 0:
                next_page_url = 'http://journals.plos.org' + next_page[0].strip()
                yield Request(next_page_url, callback=self.parse_page)

    def parse_item(self, response):
        item = SpideroneItem()
        item['xml_url'] = response.url + "&type=manuscript"
        item['text_url'] = response.url
        item['subject'] = (response.xpath('//meta[@name = "keywords"]/@content').extract())[0]
        item['count'] = self.count
        self.count += 1

        # get article's abstract
        abs = ""
        abstract = (response.xpath('//div[@class="abstract toc-section"]//p'))

        if len(abstract) != 0:
            for i in abstract:
                s = i.xpath('string(.)').extract()[0]
                abs = abs + str(s)
        item['abstract'] = abs

        # get article's introduction

        bac = ""
        background = response.xpath('//div[@class="article-text"]/div[not(contains(@class,"abstract '
                                    'toc-section"))]//a[@title="Background"]//following-sibling::p|//div['
                                    '@class="article-text"]/div[not(contains(@class,"abstract toc-section"))]//a['
                                    '@title="Background"]//following-sibling::div[@class="section toc-section"]/p')
        if len(background) != 0:
            for i in background:
                s = i.xpath('string(.)').extract()[0]
                bac = bac + str(s)

        intr = ""
        introduction = response.xpath('//div[@class="article-text"]/div[not(contains(@class,"abstract '
                                      'toc-section"))]//a[@title="Introduction"]//following-sibling::p|//div['
                                      '@class="article-text"]/div[not(contains(@class,"abstract toc-section"))]//a['
                                      '@title="Introduction"]//following-sibling::div[@class="section '
                                      'toc-section"]/p')
        if len(introduction) != 0:
            for i in introduction:
                s = i.xpath('string(.)').extract()[0]
                intr = intr + str(s)

        item['introduction'] = intr + bac

        # get article's methods
        # online = ""
        # onlinemethods = (response.xpath('//div[@class="article-text"]/div[not(contains(@class,"abstract toc-section"))]//a['
        #                             '@title="Online methods"]/following-sibling::p|//div[@class="article-text"]/div[not('
        #                             'contains(@class,"abstract toc-section"))]//a['
        #                             '@title="Online methods"]//following-sibling::div[@class="section toc-section"]/p'))
        # if len(onlinemethods) != 0:
        #     for i in onlinemethods:
        #         s = i.xpath('string(.)').extract()[0]
        #         online = online + str(s)
        #

        ma1 = ""
        Materials1 = (response.xpath('//div[@class="article-text"]/div[not(contains(@class,"abstract '
                                     'toc-section"))]//a[contains(@title,"and method")]/following-sibling::p|//div['
                                     '@class="article-text"]/div[not(contains(@class,"abstract toc-section"))]//a['
                                     'contains(@title,"and method")]//following-sibling::div[@class="section '
                                     'toc-section"]/p'))
        if len(Materials1) != 0:
            for i in Materials1:
                s = i.xpath('string(.)').extract()[0]
                ma1 = ma1 + str(s)
        mat = ""
        Materials = (response.xpath('//div[@class="article-text"]/div[not(contains(@class,"abstract '
                                    'toc-section"))]//a[contains(@title,"and methods")]/following-sibling::p|//div['
                                    '@class="article-text"]/div[not(contains(@class,"abstract toc-section"))]//a['
                                    'contains(@title,"and methods")]//following-sibling::div[@class="section '
                                    'toc-section"]/p'))
        if len(Materials) != 0:
            for i in Materials:
                s = i.xpath('string(.)').extract()[0]
                mat = mat + str(s)

        mets = ""
        methods = (response.xpath('//div[@class="article-text"]/div[not(contains(@class,"abstract toc-section"))]//a['
                                  'contains(@title,"Methods") '
                                  ']/following-sibling::p|//div[@class="article-text"]/div[not('
                                  'contains(@class,"abstract toc-section"))]//a['
                                  'contains(@title,"Methods")]//following-sibling::div[@class="section toc-section"]/p'))
        if len(methods) != 0:
            for i in methods:
                s = i.xpath('string(.)').extract()[0]
                mets = mets + str(s)
        item['methods'] = mets + mat + ma1
        # + mat
        # get article's results
        resul = ""
        results = (response.xpath('//div[@class="article-text"]/div[not(contains(@class,"abstract '
                                  'toc-section"))]//a[@title="Results"]/following-sibling::p|//div['
                                  '@class="article-text"]/div[not(contains(@class,"abstract toc-section"))]//a['
                                  '@title="Results"]//following-sibling::div[@class="section toc-section"]/p'))
        if len(results) != 0:
            for i in results:
                s = i.xpath('string(.)').extract()[0]
                resul = resul + str(s)
        item['results'] = resul

        # get article's discussion and conclusions
        conc = ""
        conclusions = (response.xpath('//div[@class="article-text"]/div[not(contains(@class,"abstract '
                                      'toc-section"))]//a[contains(@title,"Conclusions")]/following-sibling::p|//div['
                                      '@class="article-text"]/div[not(contains(@class,"abstract toc-section"))]//a['
                                      'contains(@title,"Conclusion")]//following-sibling::div[@class="section toc-section"]/p'))
        if len(conclusions) != 0:
            for i in conclusions:
                s = i.xpath('string(.)').extract()[0]
                conc = conc + str(s)

        dis = ""
        discussion = (response.xpath('//div[@class="article-text"]/div[not(contains(@class,"abstract '
                                     'toc-section"))]//a[contains(@title,"Discussion")]/following-sibling::p|//div['
                                     '@class="article-text"]/div[not(contains(@class,"abstract toc-section"))]//a['
                                     'contains(@title,"Discussion")]//following-sibling::div[@class="section toc-section"]/p'))
        if len(discussion) != 0:
            for i in discussion:
                s = i.xpath('string(.)').extract()[0]
                dis = dis + str(s)

        item['discussion'] = dis + conc

        # clean up text
        for key in item.keys():
            if key == 'count' or key == 'text_url':
                continue
        #
            # remove tags, dangling whitespace, and citations
            # fix ampersand characters and spaces before periods
            item[key] = re.sub('\|', '', item[key])
            item[key] = re.sub('\n','',item[key])
            item[key] = item[key].strip()
        #     item[key] = item[key].replace('&amp;', '&')
        #     item[key] = re.sub('\[.*\]', '', item[key])
        #     item[key] = re.sub(' \.', '.', item[key])

        return item


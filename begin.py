# coding=utf-8
from scrapy import cmdline

cmdline.execute("scrapy crawl testone -o results\\another.csv".split())
from datetime import datetime
from scrapy.crawler import CrawlerProcess
import scrapy
import csv
import sys

class TableScraper(scrapy.Spider):
    name = 'table_scraper'

    def parse(self, response):
        print('Parsing response from {}'.format(response.url))
        response = response.replace(body=response.body.replace(b'<br/>', b' '))
        print('Collecting header row...')
        header = self.parse_table_as_csv(
            response, '//table//thead', '//th//text()')
        print('Collecting body rows...')
        body = self.parse_table_as_csv(
            response, '//table//tbody//tr', 'td//text()')
        with open('{}_result_table_scraper.csv'.format(datetime.now().strftime('%Y%m%d%H%M%S')), 'w') as f:
            writer = csv.writer(f)
            writer.writerows(header)
            writer.writerows(body)

    def parse_table_as_csv(self, response, row_selector, col_selector):
        result = []
        rows = response.xpath(row_selector)
        for index, row in enumerate(rows):
            cols = row.xpath(col_selector)
            row_result = []
            for col in cols:
                row_result.append(col.extract().strip())
            result.append(row_result)
            print('Collected {}/{}: \"{},...\"'.format(index + 1, len(rows), row_result[0]))
        return result

process = CrawlerProcess()
process.crawl(TableScraper, start_urls=sys.argv[1:])
process.start()
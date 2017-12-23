import scrapy

class FirstSpider(scrapy.Spider):
    name = 'first_spider'
    start_urls = ['http://www.muabannhadat.vn/dat-ban-3515/tp-da-nang-s31', ]

    main_url = 'http://www.muabannhadat.vn'

    def parse(self, response):
        item_selector = '.resultItem'
        items = response.css(item_selector)

        for item in items:
            title_selector = '.title-filter-link ::text'
            title = item.css(title_selector).extract_first()

            address_selector = './div[2]/div[2]/div[2]/text()'
            address = item.xpath(address_selector).extract_first()

            print(title)
            print(address)

        next_page_selector = './ul/li[@id="MainContent_ctlList_ctlResults_ctlPager_liNext"]/a/@href'
        next_page = response.css('.list-footer').xpath(next_page_selector).extract_first()
        print("next page: ", next_page)

        if next_page:
            yield response.follow(self.main_url + next_page, self.parse)





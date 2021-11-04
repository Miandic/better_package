import scrapy


class ParecdekSpider(scrapy.Spider):
    name = 'PareCDEK'
    allowed_domains = ['https://cdek.kz/ru/calculate']
    start_urls = ['http://https://cdek.kz/ru/calculate/']

    def parse(self, response):
        pass

    def get_Date(self, response):
        money = response.css(".calculator-service__price::text").extract()
        timeCargo = response.css(".calculator-service__price::text").extract()
        all_data = zip(money, timeCargo)
        returned_info = [["CDEK", 0, 0], ["CDEK", 0, 0], ["CDEK", 0, 0]]
        mx = 0
        i = 0
        for item in all_data:
            if (returned_info[0][0] < item[0]):
                returned_info[0][0] = item[0]
                returned_info[0][1] = item[1]

            if (returned_info[2][1] > item[1]):
                returned_info[2][0] = item[0]
                returned_info[2][1] = item[1]

            returned_info[1][0] += item[0]
            returned_info[1][1] += item[1]
            i += 1
        returned_info[1][0] /= i

        returned_info[1][1] /= i

        return returned_info



import requests
import scrapy
from bs4 import BeautifulSoup


class company:
    def __init__(self, start_point, end_point, currency, weight, height, width):
        self.start_point = start_point
        self.end_point = end_point
        self.currency = currency
        self.weight = weight
        self.height = height
        self.width = width

    def get_data(self):
        pass

    def get_data(self):
        pass


class ParsCDEK(company):
    def __init__(self, start_point, end_point, currency, weight, height, width):
        company.__init__(self, start_point, end_point, currency, weight, height, width)

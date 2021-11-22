from selenium import webdriver
from Parser.Functions import xpath_soup


class Company:
    def __init__(self, start_point, end_point, currency, length, weight, height, width, money):
        self.start_point = start_point
        self.end_point = end_point
        self.currency = currency
        self.weight = weight
        self.height = height
        self.width = width
        self.length = length
        self.money_recent = money
        self.money = 0
        self.time = 0
        self.name = ""
        self.returned_data = []

        self.driver = webdriver.Chrome(executable_path=r'webdriver.exe')

    def to_xpath(self, name):
        xpath = xpath_soup(name)
        return self.driver.find_element_by_xpath(xpath)

    def set_data(self):
        pass

    def write_data(self):
        pass

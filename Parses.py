import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import urllib
import warnings
import requests
import json
import time
from datetime import date
from selenium.webdriver.common.action_chains import ActionChains
import itertools
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

warnings.filterwarnings("ignore", category=UserWarning, module='bs4')


def cnt_time(a, b):
    c = date.today()
    c = c.year
    a1 = list(map(str, a.split()))
    b1 = list(map(str, b.split()))
    if (c % 4 == 0 and c % 100 != 0):
        days = {"янв": 0, "фев": 31, "мар": 60, "апр": 91, "май": 121, "июн": 152, "июл": 182, "авг": 213, "сен": 244,
                "окт": 274,
                "ноя": 305, "дек": 335}
    else:
        days = {"янв": 0, "фев": 31, "мар": 59, "апр": 90, "май": 120, "июн": 151, "июл": 181, "авг": 212, "сен": 243,
                "окт": 273,
                "ноя": 304, "дек": 334}
    if (int(b1[0]) + days[b1[1]] >= int(a1[0]) + days[a1[1]]):
        return (int(b1[0]) + days[b1[1]] - int(a1[0]) - days[a1[1]])
    elif (c % 4 == 0 and c % 100 != 0):
        return (366 - int(a1[0]) - days[a1[1]] + int(b1[0]) + days[b1[1]])
    else:
        return (365 - int(a1[0]) - days[a1[1]] + int(b1[0]) - days[b1[1]])


def xpath_soup(element):
    components = []
    child = element if element.name else element.parent
    for parent in child.parents:
        previous = itertools.islice(parent.children, 0, parent.contents.index(child))
        xpath_tag = child.name
        xpath_index = sum(1 for i in previous if i.name == xpath_tag) + 1
        components.append(xpath_tag if xpath_index == 1 else '%s[%d]' % (xpath_tag, xpath_index))
        child = parent
    components.reverse()
    return '/%s' % '/'.join(components)


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
        self.returned_data = [[]]

    def to_xpath(self, name):
        xpath = xpath_soup(name)
        return self.driver.find_element_by_xpath(xpath)

    def set_data(self):
        pass

    def write_data(self):
        pass

    def return_json(self):
        r = {
            'Cost': self.money,
            'Name': self.name,
            'Date': self.time
        }
        return r


class ParsDel(Company):
    def __init__(self, start_point, end_point, currency, length, weight, height, width, money):
        Company.__init__(self, start_point, end_point, currency, length, weight, height, width, money)
        self.name = "DelLine"

        self.driver = webdriver.Chrome(executable_path=r'C:\Users\Никита\Downloads\chromedriver.exe')
        self.url = 'https://www.dellin.ru/requests/'
        self.driver.get(self.url)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 20)

        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')

    # func for simple_input and hard_input
    # simple_input - witout dropmenu_click
    # hard_input with dropmenu_click and sleep
    def parse_propetry_simple_input(self, parametr, find_parametr):
        path_soup = self.soup.find("input", {"id": find_parametr})
        selenium_path_element = self.to_xpath(path_soup)
        ActionChains(self.driver).move_to_element(selenium_path_element).click().send_keys(parametr).perform()

    def parse_propetry_hard_input(self, parametr, find_parametr):
        selenium_path_element = self.soup.find("input", {"id": find_parametr})
        selenium_element2 = self.to_xpath(selenium_path_element)
        ActionChains(self.driver).move_to_element(selenium_element2).click().send_keys(parametr,
                                                                                       ).perform()
        time.sleep(1)

        ActionChains(self.driver).send_keys(
            Keys.ENTER).perform()
        time.sleep(1)

        ActionChains(self.driver).send_keys(
            Keys.ENTER).perform()

    def write_data(self):
        # input lenght, widht,height,weight  value on delLine site
        self.parse_propetry_simple_input(self.length, "length_view")

        self.parse_propetry_simple_input(self.width, "width_view")

        self.parse_propetry_simple_input(self.height, "height_view")

        self.parse_propetry_simple_input(self.weight, "sized_weight")

        # input for cheracter, derival and arrival point
        self.parse_propetry_hard_input("Личные вещи (переезд)", "freight_name")

        self.parse_propetry_hard_input(self.start_point, "derival_point")

        self.parse_propetry_hard_input(self.end_point, "arrival_point")

    def read_data(self):
        time.sleep(5)
        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        self.returned_data[0].append(self.name)
        dateAll = self.soup.findAll("span", {"class": "date"})
        a = dateAll[0].text
        a = str(a).strip()
        b = dateAll[-1].text
        b = str(b).strip()
        for i in range(len(a)):
            if not a[i].isnumeric():
                a = a[:i] + ' ' + a[i:len(a)]
        for i in range(len(b)):
            if not b[i].isnumeric():
                b = b[:i] + ' ' + b[i:len(b)]

        cost = self.soup.find("span", {"class": "bill-total"})

        self.returned_data[0].append(cost.text)
        self.returned_data[0].append(cnt_time(a, b))

    def return_info(self):
        print(self.returned_data)


class ParseCDEK(Company):
    def __init__(self, start_point, end_point, currency, length, weight, height, width, money):
        Company.__init__(self, start_point, end_point, currency, length, weight, height, width, money)
        self.name = "DelLine"

        self.driver = webdriver.Chrome(executable_path=r'C:\Users\Никита\Downloads\chromedriver.exe')
        self.url = 'https://www.cdek.ru/ru/calculate'
        self.driver.get(self.url)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 20)

        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')

    # func for simple_input
    # simple_input
    def parse_propetry_simple_input(self, value, find_parametr, find_parametr_property):
        path_soup = self.soup.find("input", {find_parametr: find_parametr_property})
        selenium_path_element = self.to_xpath(path_soup)
        ActionChains(self.driver).move_to_element(selenium_path_element).click().send_keys(value).perform()

    def write_data(self):
        inputs = self.soup.findAll("input", {"class": "autocomplete-parcel__control"})
        selenium_path_element = self.to_xpath(inputs[0])
        ActionChains(self.driver).move_to_element(selenium_path_element).click().send_keys(self.start_point).perform()
        time.sleep(2)

        selenium_path_element = self.to_xpath(inputs[1])
        ActionChains(self.driver).move_to_element(selenium_path_element).click().send_keys(self.end_point).perform()
        time.sleep(2)

        path_soup = self.soup.find("input", {"class": "base-control-old__field"})
        selenium_path_element = self.to_xpath(path_soup)
        ActionChains(self.driver).move_to_element(selenium_path_element).click().perform()
        time.sleep(2)
        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')

        path_soup = self.soup.findAll("button", {"class": "choice-tabs__action"})
        selenium_path_element = self.to_xpath(path_soup[1])
        ActionChains(self.driver).move_to_element(selenium_path_element).click().perform()

    def read_data(self):
        time.sleep(5)
        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        self.returned_data[0].append(self.name)
        dateAll = self.soup.findAll("span", {"class": "date"})
        a = dateAll[0].text
        a = str(a).strip()
        b = dateAll[-1].text
        b = str(b).strip()
        for i in range(len(a)):
            if not a[i].isnumeric():
                a = a[:i] + ' ' + a[i:len(a)]
        for i in range(len(b)):
            if not b[i].isnumeric():
                b = b[:i] + ' ' + b[i:len(b)]

        cost = self.soup.find("span", {"class": "bill-total"})

        self.returned_data[0].append(cost.text)
        self.returned_data[0].append(cnt_time(a, b))

    def return_info(self):
        print(self.returned_data)


# self, start_point, end_point, currency, length , weight, height, width ,  money
a = ParseCDEK("Москва", "Ростов", "rub", "1", "0.2", "0.3", "0.3", "1500")
a.write_data()

#a.read_data()
"""
print(a.returned_data)
exit(a.returned_data)
"""
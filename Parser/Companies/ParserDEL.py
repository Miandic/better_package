from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from Parser.Companies.Company import Company
from Parser.Functions import xpath_soup, cnt_time


class ParserDEL(Company):
    def __init__(self, start_point, end_point, currency, length, weight, height, width, money):
        Company.__init__(self, start_point, end_point, currency, length, weight, height, width, money)
        self.name = "DelLine"

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

        self.read_data()

        print(self.returned_data)

    def read_data(self):
        time.sleep(5)
        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        self.returned_data.append(self.name)
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

        self.returned_data.append(cost.text)
        self.returned_data.append(cnt_time(a, b))

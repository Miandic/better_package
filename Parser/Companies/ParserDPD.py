from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from Parser.Companies.Company import Company
from Parser.Functions import xpath_soup, cnt_time

#xui
class ParserDPD(Company):
    def __init__(self, start_point, end_point, currency, length, weight, height, width, money):
        Company.__init__(self, start_point, end_point, currency, length, weight, height, width, money)
        self.name = "DPD"

        self.url = 'https://www.dpd.ru/ols/calc/calc.do2'
        self.driver.get(self.url)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 20)

        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')

    def parse_propetry_simple_input(self, parametr, find_parametr):
        path_soup = self.soup.find("input", {"id": find_parametr})
        selenium_path_element = self.to_xpath(path_soup)
        ActionChains(self.driver).move_to_element(selenium_path_element).click().send_keys(parametr).perform()

    def parse_propetry_hard_input(self, parametr, find_parametr):
        selenium_path_element = self.soup.find("input", {"id": find_parametr})
        selenium_element2 = self.to_xpath(selenium_path_element)

        print(selenium_element2)

        ActionChains(self.driver).move_to_element(selenium_element2).click().send_keys(parametr
                                                                                       ).perform()
        time.sleep(2)

        ActionChains(self.driver).send_keys(Keys.DOWN).send_keys(
            Keys.ENTER).perform()

    def click(self):
        path_soup = self.soup.find("input", {"id": "calc_calculate_btn"})
        selenium_path_element = self.to_xpath(path_soup)
        ActionChains(self.driver).move_to_element(selenium_path_element).click().perform()

    def write_data(self):
        # input lenght, widht,height,weight  value on delLine site
        self.parse_propetry_hard_input(self.start_point, "cityOrig")

        time.sleep(1)

        self.parse_propetry_hard_input(self.end_point, "cityDest")

        time.sleep(1)

        self.parse_propetry_simple_input(self.weight, "calc_weight")

        self.parse_propetry_simple_input(str((self.height * self.width * self.length) / 1000000), "calc_volume")

        self.parse_propetry_simple_input(str(self.money_recent), "calc_declared_cost")

        self.click()

        # self.parse_propetry_simple_input(self.height[:-2]+','+self.height[-2:], "height_view")

        # self.parse_propetry_simple_input(self.weight, "sized_weight")

        # input for cheracter, derival and arrival point
        # self.parse_propetry_hard_input("Личные вещи (переезд)", "freight_name")

        # self.parse_propetry_hard_input(self.start_point, "derival_point")

        # self.parse_propetry_hard_input(self.end_point, "arrival_point")

        self.read_data()

        print(self.returned_data)

    def read_data(self):
        time.sleep(3)
        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        self.returned_data.append(self.name)
        time.sleep(2)
        dateAll = self.soup.find("input", {"id": "cost"})

        dateAll = xpath_soup(dateAll)
        dateAll = self.driver.find_element_by_xpath(dateAll)

        a = dateAll.get_attribute('value')

        dateAll = self.soup.find("input", {"id": "days"})
        dateAll = xpath_soup(dateAll)
        dateAll = self.driver.find_element_by_xpath(dateAll)

        b = dateAll.get_attribute('value')

        self.returned_data.append(a)
        self.returned_data.append(b)

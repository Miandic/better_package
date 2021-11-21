from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from Parser.Companies.Company import Company


class ParserCDEK(Company):
    def __init__(self, start_point, end_point, currency, length, weight, height, width, money):
        Company.__init__(self, start_point, end_point, currency, length, weight, height, width, money)
        self.name = "CDEK"

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
        time.sleep(2)

        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')

        path_soup = self.soup.findAll("input", {"class": "base-control__field"})

        selenium_path_element = self.to_xpath(path_soup[0])
        ActionChains(self.driver).move_to_element(selenium_path_element).click().send_keys(self.length).perform()

        selenium_path_element = self.to_xpath(path_soup[1])
        ActionChains(self.driver).move_to_element(selenium_path_element).click().send_keys(self.width).perform()

        selenium_path_element = self.to_xpath(path_soup[2])
        ActionChains(self.driver).move_to_element(selenium_path_element).click().send_keys(self.height).perform()

        selenium_path_element = self.to_xpath(path_soup[3])
        ActionChains(self.driver).move_to_element(selenium_path_element).click().send_keys(self.weight).perform()
        time.sleep(1)
        ActionChains(self.driver).move_to_element(selenium_path_element).click().send_keys(Keys.ENTER)

        path_soup = self.soup.find("button", {"class": "base-icon-button"})
        selenium_path_element = self.to_xpath(path_soup)
        ActionChains(self.driver).move_to_element(selenium_path_element).click().perform()

        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')

        path_soup = self.soup.find("button",
                                   {"class": "base-button--block base-button base-button--primary base-button--round"})
        selenium_path_element = self.to_xpath(path_soup)
        ActionChains(self.driver).move_to_element(selenium_path_element).click().perform()

        self.read_data()

        print(self.returned_data)

    def read_data(self):
        time.sleep(3)
        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        self.returned_data.append(self.name)
        cost = self.soup.find("div",
                              {"class": "info-order__total-value"})
        cost_str = cost.text
        total_cost_ans = ""
        for i in range(len(cost_str)):
            if cost_str[i].isnumeric():
                total_cost_ans += cost_str[i]

        date_arrive = self.soup.find("span", {"class": "info-order__days"})
        date_arrive_str = date_arrive.text
        total_date_arrive_ans = ""

        for i in range(len(date_arrive_str)):
            if date_arrive_str[i].isnumeric():
                total_date_arrive_ans += date_arrive_str[i]
            if date_arrive_str[i] == '-':
                total_date_arrive_ans += date_arrive_str[i]

        self.returned_data.append(total_cost_ans)
        self.returned_data.append(total_date_arrive_ans)

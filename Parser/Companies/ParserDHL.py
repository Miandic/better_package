from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from Parser.Companies.Company import Company


class ParserDHL(Company):
    def __init__(self, start_point, end_point, currency, length, weight, height, width, money):
        Company.__init__(self, start_point, end_point, currency, length, weight, height, width, money)
        self.name = "DHL"

        self.url = 'https://express.dhl.ru/calculator/'
        self.driver.get(self.url)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 20)

        self.wait = WebDriverWait(self.driver, 10)
        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')

    # func for simple_input
    # simple_input
    def parse_propetry_simple_input(self, value, find_parametr, find_parametr_property):
        path_soup = self.soup.find("input", {find_parametr: find_parametr_property})
        selenium_path_element = self.to_xpath(path_soup)
        ActionChains(self.driver).move_to_element(selenium_path_element).click().send_keys(value).perform()

    def write_data(self):
        inputs = self.soup.findAll("input", {"required": "required"})
        # inputs[1] from place in the country
        selenium_path_element = self.to_xpath(inputs[1])
        ActionChains(self.driver).move_to_element(selenium_path_element).click().send_keys(self.start_point).perform()
        time.sleep(3)
        # inputs[3] where take cargo from country in inputs[2]
        selenium_path_element = self.to_xpath(inputs[3])
        ActionChains(self.driver).move_to_element(selenium_path_element).click().send_keys(self.end_point).perform()
        time.sleep(2)
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        time.sleep(2)
        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')

        input = self.soup.find("a", {"href": "#"})
        selenium_path_element = self.to_xpath(input)
        ActionChains(self.driver).move_to_element(selenium_path_element).click().perform()

        input = self.soup.find("input", {"placeholder": "Вес"})
        selenium_path_element = self.to_xpath(input)
        ActionChains(self.driver).move_to_element(selenium_path_element).click().send_keys(self.weight).perform()

        button = self.soup.findAll("button", {"class": "tab-button"})
        selenium_path_element = self.to_xpath(button[1])
        ActionChains(self.driver).move_to_element(selenium_path_element).click().send_keys(self.weight).perform()

        time.sleep(1)
        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        time.sleep(1)

        widht = self.soup.find("input", {"placeholder": "Ширина"})
        selenium_path_element = self.to_xpath(widht)
        ActionChains(self.driver).move_to_element(selenium_path_element).click().send_keys(self.width).perform()

        height = self.soup.find("input", {"placeholder": "Высота"})
        selenium_path_element = self.to_xpath(height)
        ActionChains(self.driver).move_to_element(selenium_path_element).click().send_keys(self.height).perform()

        lenght = self.soup.find("input", {"placeholder": "Длина"})
        selenium_path_element = self.to_xpath(lenght)
        ActionChains(self.driver).move_to_element(selenium_path_element).click().send_keys(self.length).perform()

        time.sleep(1)
        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        time.sleep(1)

        button_ready = self.soup.findAll("button")
        selenium_path_element = self.to_xpath(button_ready[3])
        ActionChains(self.driver).move_to_element(selenium_path_element).click().perform()

        time.sleep(2)
        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')

        button = self.soup.find("button", {"class": "button-icon full"})
        selenium_path_element = self.to_xpath(button)
        ActionChains(self.driver).move_to_element(selenium_path_element).click().perform()

        self.read_data()

        print(self.returned_data)

    def read_data(self):
        time.sleep(8)
        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        time.sleep(5)
        cost = self.soup.find("div", {"class": "calculated-item__price-value"})
        cost = cost.text
        cost_cif = ""
        for i in range(len(cost)):
            if cost[i].isnumeric(): cost_cif += cost[i]

        date = self.soup.find("span", {"class": "date"})

        date = date.text
        date_cif = ""
        for i in range(len(date)):
            if date[i].isnumeric(): date_cif += date[i]

        self.returned_data.append(self.name)

        self.returned_data.append(cost_cif)

        self.returned_data.append(date_cif)

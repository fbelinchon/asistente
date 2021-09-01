from selenium import webdriver
from bs4 import BeautifulSoup

class infow():
    def __init__(self):
        self.driver=webdriver.Chrome(executable_path="C:/Users/Francisco/Downloads/chromedriver.exe")
    
    def get_info(self,query):
        text=""
        self.query=query
        self.driver.get(url="https://es.wikipedia.org")
        search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element_by_xpath('//*[@id="searchButton"]')
        enter.click()
        data=self.driver.find_element_by_xpath('//*[@class="mw-parser-output"]/p')
        text=data.text
        self.driver.close()
        return text

def cleanHtml(text):
    return BeautifulSoup(text,"lxml").text





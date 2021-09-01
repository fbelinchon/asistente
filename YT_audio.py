from selenium import webdriver

class music():
    def __init__(self):
        self.driver=webdriver.Chrome(executable_path="C:/Users/Francisco/Downloads/chromedriver.exe")

    def play(self,query):
        self.query = query
        self.driver.get(url='https://www.youtube.com/results?search_query=' + query)
        acepto=self.driver.find_element_by_xpath('//yt-formatted-string[text()="Acepto"]')
        acepto.click()
        video = self.driver.find_element_by_xpath('//yt-img-shadow[1]')
        video.click()


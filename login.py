from selenium import webdriver
from confidential import username, password


class Bot:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def blackboard(self):
        self.driver.get('https://blackboard.usiu.ac.ke/webbapps/login')

        consent = self.driver.find_element_by_xpath('//*[@id="agree_button"]')
        consent.click()

        Username = self.driver.find_element_by_xpath('//*[@id="user_id"]')
        Username.click()
        Username.send_keys(username)

        pwd = self.driver.find_element_by_xpath('//*[@id="password"]')
        pwd.click()
        pwd.send_keys(password)

        login = self.driver.find_element_by_xpath('//*[@id="entry-login"]')
        login.click()

    


bot = Bot()
bot.blackboard()
bot.blackboard_breach()
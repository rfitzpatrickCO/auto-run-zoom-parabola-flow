from selenium import webdriver

class ParabolaBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")

ParabolaBot()
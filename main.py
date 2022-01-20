import imp
from lib2to3.pgen2 import driver
from multiprocessing.connection import wait
from selenium import webdriver
from time import sleep
from secrets import myUsername
from secrets import myPassword

# This script is used to automate the process of managing Zoom licenses
# with the use of Parabola.io. In order to avoid paying for Parabola
# to schedule workflows, this script will run automatically
# to log me in and run the workflow.

class ParabolaBot:
    def __init__(self, username, myPassword):
        self.driver = webdriver.Chrome()
# Go to Parabola and log in with username and password
        self.driver.get("example.com")
        sleep(2)
        login_field = self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        login_field = self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(myPassword)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)
# Click on the Zoom License Manager flow in my dasboard
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div/div[1]").click()
        sleep(2)
# Click on Run Flow Now
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/button").click()
        sleep(2)
# Confirm by clicking on Run Now
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div/div[1]/section/div[1]/div[1]/div/div/div[2]/div[2]/form/button").click()
        sleep(60)


ParabolaBot(myUsername , myPassword)
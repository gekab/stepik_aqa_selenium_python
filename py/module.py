import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def registration(browser):
    input1 = browser.find_element(by='name', value="first_name")
    input1.send_keys("Ivan")
    input2 = browser.find_element(by='name', value="last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(by='class name', value='form-control.city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(by='id', value="country")
    input4.send_keys("Russia")
    button = browser.find_element(by='css selector', value="button.btn")
    button.click()
    print(browser.switch_to.alert.text)
    time.sleep(10)


def registration_xpath(browser):
    input1 = browser.find_element(by='name', value="first_name")
    input1.send_keys("Ivan")
    input2 = browser.find_element(by='name', value="last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(by='class name', value='form-control.city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(by='id', value="country")
    input4.send_keys("Russia")
    button = browser.find_element(by='xpath', value="//button[contains(text(), 'Submit')]")
    button.click()
    time.sleep(10)
    print(browser.switch_to.alert.text)



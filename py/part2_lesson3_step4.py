from selenium import webdriver
from module import calc
import time

try:
    # 1. Открыть страницу http://suninjuly.github.io/alert_accept.html
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
    # 2. Нажать на кнопку
    browser.find_element(by='class name', value='btn.btn-primary').click()
    # 3. Принять confirm
    browser.switch_to.alert.accept()
    # 4. На новой странице решить капчу для роботов, чтобы получить число с ответом
    x = calc(browser.find_element(by='id', value='input_value').text)
    browser.find_element(by='id', value='answer').send_keys(x)
    browser.find_element(by='class name', value='btn.btn-primary').click()
    print(browser.switch_to.alert.text.split(':')[1])
finally:
    time.sleep(1)
    browser.quit()

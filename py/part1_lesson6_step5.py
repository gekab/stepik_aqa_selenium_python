import time
from selenium import webdriver
import math
from module import registration
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_link_text"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    val = str(math.ceil(math.pow(math.pi, math.e) * 10000))
    print(val)
    elem = browser.find_element(by='link text', value=val)
    elem.click()
    registration(browser)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

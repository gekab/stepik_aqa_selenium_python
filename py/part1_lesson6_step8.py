import time
from selenium import webdriver
from module import registration_xpath

link = "http://suninjuly.github.io/find_xpath_form"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    registration_xpath(browser)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

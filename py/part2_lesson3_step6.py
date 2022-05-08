from selenium import webdriver
import time
from module import calc

try:
    # 1. Открыть страницу http://suninjuly.github.io/redirect_accept.html
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
    # 2. Нажать на кнопку
    browser.find_element(by='class name', value='trollface.btn.btn-primary').click()
    # 3. Переключиться на новую вкладку
    browser.switch_to.window(browser.window_handles[1])
    # 4. Пройти капчу для робота и получить число-ответ
    x = calc(browser.find_element(by='id', value='input_value').text)
    browser.find_element(by='id', value='answer').send_keys(x)
    browser.find_element(by='class name', value='btn.btn-primary').click()
    print(browser.switch_to.alert.text.split(':')[1])

finally:
    time.sleep(2)
    browser.quit()

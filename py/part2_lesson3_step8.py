from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from module import calc

try:
    # 1. Открыть страницу http://suninjuly.github.io/explicit_wait2.html
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    # 2. Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    # говорим Selenium проверять в течение 15 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), text_='$100')
    )
    # 3. Нажать на кнопку "Book"
    browser.find_element(by='id', value='book').click()
    # 4. Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
    x = calc(browser.find_element(by='id', value='input_value').text)
    browser.find_element(by='id', value='answer').send_keys(x)
    browser.find_element(by='id', value='solve').click()
    print(browser.switch_to.alert.text.split(':')[1])
finally:
    browser.quit()

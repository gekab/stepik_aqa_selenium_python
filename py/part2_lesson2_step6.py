from selenium import webdriver
import time
from module import calc
from selenium.webdriver.support.ui import Select


try:
    # 1. Открыть страницу http://SunInJuly.github.io/execute_script.html.
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # 2. Считать значение для переменной x.
    x_element = browser.find_element(by='id', value='input_value')
    x = x_element.text
    # 3. Посчитать математическую функцию от x.
    y = calc(x)
    # 4. Проскроллить страницу вниз.
    button = browser.find_element(by='class name', value='btn.btn-primary')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    # 5. Ввести ответ в текстовое поле.
    browser.find_element(by='id', value='answer').send_keys(y)
    # 5. Отметить checkbox "I'm the robot".
    browser.find_element(by='id', value='robotCheckbox').click()
    # 6. Выбрать radiobutton "Robots rule!".
    browser.find_element(by='id', value='robotsRule').click()
    # 8. Нажать на кнопку "Submit".
    browser.find_element(by='class name', value='btn.btn-primary').click()
    # 9. Распечатать ответ с Alert в консоль.
    print(browser.switch_to.alert.text)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

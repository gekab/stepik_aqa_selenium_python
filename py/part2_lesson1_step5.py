from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Код, который заполняет обязательные поля
    x_element = browser.find_element(by='id', value='input_value')
    x = x_element.text
    y = calc(x)
    # 4. Ввести ответ в текстовое поле.
    browser.find_element(by='id', value='answer').send_keys(y)
    # 5. Отметить checkbox "I'm the robot".
    browser.find_element(by='id', value='robotCheckbox').click()

    # 6. Выбрать radiobutton "Robots rule!".
    browser.find_element(by='id', value='robotsRule').click()

    # 7. Нажать на кнопку Submit.
    browser.find_element(by='class name', value='btn.btn-default').click()
    
    # 8. Распечатать ответ с Alert в консоль.
    print(browser.switch_to.alert.text)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

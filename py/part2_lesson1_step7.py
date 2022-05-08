from selenium import webdriver
import time
import math
from part2_lesson1_step5 import calc


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    # 1. Открыть страницу http://suninjuly.github.io/get_attribute.html.
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # 2. Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
    img_element = browser.find_element(by='id', value='treasure')
    # 3. Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
    get_attr = img_element.get_attribute('valuex')
    # 4. Посчитать математическую функцию от x (сама функция остаётся неизменной).
    f = calc(get_attr)
    # 5. Ввести ответ в текстовое поле.
    browser.find_element(by='id', value='answer').send_keys(f)
    # 6. Отметить checkbox "I'm the robot".
    browser.find_element(by='id', value='robotCheckbox').click()
    # 7. Выбрать radiobutton "Robots rule!".
    browser.find_element(by='id', value='robotsRule').click()
    # 8. Нажать на кнопку "Submit".
    browser.find_element(by='class name', value='btn.btn-default').click()


    # 8. Распечатать ответ с Alert в консоль.
    print(browser.switch_to.alert.text)



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


try:
    # 1. Открыть страницу http://suninjuly.github.io/selects1.html
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # 2. Посчитать сумму заданных чисел
    num1 = int(browser.find_element(by='id', value='num1').text)
    num2 = int(browser.find_element(by='id', value='num2').text)
    sum_num1_num2 = str(num1 + num2)
    # 3. Выбрать в выпадающем списке значение равное расчитанной сумме
    select = Select(browser.find_element(by='id', value='dropdown'))
    select.select_by_value(sum_num1_num2)
    # 4. Нажать кнопку "Submit"
    browser.find_element(by='class name', value='btn.btn-default').click()
    # 8. Распечатать ответ с Alert в консоль.
    print(browser.switch_to.alert.text)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

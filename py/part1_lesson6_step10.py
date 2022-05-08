from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Код, который заполняет обязательные поля
    first_name = browser.find_element(by='class name', value="first_block .first")
    first_name.send_keys("Ivan")
    last_name = browser.find_element(by='class name', value="first_block .second")
    last_name.send_keys("Ivanov")
    email = browser.find_element(by='class name', value="first_block .third")
    email.send_keys("Ivan@gmail.com")

    # Отправляем заполненную форму
    button = browser.find_element(by='css selector', value="button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(by='tag name', value="h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
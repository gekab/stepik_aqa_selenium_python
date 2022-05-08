from selenium import webdriver
import time
import os

try:
    # 1. Открыть страницу http://suninjuly.github.io/file_input.html
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)
    # 2. Заполнить текстовые поля: имя, фамилия, email
    browser.find_element(by='name', value='firstname').send_keys('Vasya')
    browser.find_element(by='name', value='lastname').send_keys('Ivaniv')
    browser.find_element(by='name', value='email').send_keys('Vasya@gmail.com')
    # 3. Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    # file_path.send_keys(file_path)
    browser.find_element(by='name', value='file').send_keys(file_path)
    # 4. Нажать кнопку "Submit"
    browser.find_element(by='class name', value='btn.btn-primary').click()
    message = browser.switch_to.alert.text
    print(message.split(':')[-1])
finally:
    time.sleep(1)
    browser.quit()

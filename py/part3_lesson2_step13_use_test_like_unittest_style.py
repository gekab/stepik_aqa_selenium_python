import unittest
from selenium import webdriver


class TestLogin(unittest.TestCase):
    def test_LoginPass(self):
        link = "http://suninjuly.github.io/registration1.html"
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
        # time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(by='tag name', value="h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        expected_text = "Congratulations! You have successfully registered!"
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, expected_text, f"Test failed, got '{welcome_text}' instead of '{expected_text}'")
        browser.quit()

    def test_LoginFailed(self):
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
        # time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(by='tag name', value="h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        expected_text = "Congratulations! You have successfully registered!"
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, expected_text, f"Test failed, got '{welcome_text}' instead of '{expected_text}'")
        browser.quit()


if __name__ == "__main__":
    unittest.main()
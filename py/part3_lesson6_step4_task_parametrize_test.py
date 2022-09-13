import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

links = ["https://stepik.org/lesson/236895/step/1",
         "https://stepik.org/lesson/236896/step/1",
         "https://stepik.org/lesson/236897/step/1",
         "https://stepik.org/lesson/236898/step/1",
         "https://stepik.org/lesson/236899/step/1",
         "https://stepik.org/lesson/236903/step/1",
         "https://stepik.org/lesson/236904/step/1",
         "https://stepik.org/lesson/236905/step/1"
         ]

@pytest.mark.parametrize('site', links)
def test_guest_should_see_login_link(browser, site):
    link = site
    browser.get(link)

    answer = math.log(int(time.time()))
    text_area = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".ember-text-area")))
    text_area.send_keys(str(answer))

    submit_btn = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".submit-submission")))
    submit_btn.click()

    correct = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
    assert correct.text == "Correct!", 'Відповідь невірна!'
    time.sleep(2)
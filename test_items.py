import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_spanish_localization(browser):
    browser.get(link)
    time.sleep(30)
    button = WebDriverWait(browser, 5)\
        .until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn-add-to-basket")))
    assert button is not None, "Button not found"

from selenium.common.exceptions import NoSuchElementException
import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_item(browser):
    browser.get(link)
    try:
        find = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    except NoSuchElementException: 
        print("no such element")
        find = None
    #time.sleep(20)
    assert find is not None, "no such element"

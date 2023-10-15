import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_contains_add_to_cart_button(browser):
    browser.get(link)
    butt = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert butt, "Кнопка для добавления в корзину не найдена"
    #time.sleep(30)

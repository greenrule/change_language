import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_consist_add_to_basket(browser):
    browser.get(link)
    button = browser.find_element_by_id('add_to_basket_form')
    
    assert button.text, "Тест пройден"


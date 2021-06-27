# Gyakorlás képpen keress ki elemekt a képernyőről az alábbi kritériumoknak megfelelően:
# ID alapján
# NAME alapján
# XPath kifejezéssel Minden megtalált elemnek irassd ki a text értékét, vagy egy attribútum értékét.

from selenium import webdriver

browser = webdriver.Chrome()
URL = "http://localhost:9999/kitchensink.html"

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(URL)
# ID
mousehover = browser.find_element_by_id("mousehover")
print(mousehover.text)
# name
show_hide = browser.find_element_by_name("show-hide")
print(show_hide.get_attribute('type'))
# xpath
chbox_benz = browser.find_element_by_xpath('//*[@id="benzcheck"]')
print(chbox_benz.tag_name)

browser.close()

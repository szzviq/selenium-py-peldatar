from selenium import webdriver


URL = "http://localhost:9999/todo.html"

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(URL)
todo = []
todo = browser.find_elements_by_xpath('//li/span')
# ha a bepipált érdekelne, akkor //li/*[@class="done-true"]
for i in todo:
    print(i.text)
browser.close()
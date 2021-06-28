from selenium import webdriver
import time
URL = "http://localhost:9999/trickyelements.html"

browser = webdriver.Chrome()
try:
    browser.maximize_window()
    browser.get(URL)
    elemek = []
    elem1 = browser.find_element_by_id('element1')
    elemek.append(elem1)
    elem2 = browser.find_element_by_id('element2')
    elemek.append(elem2)
    elem3 = browser.find_element_by_id('element3')
    elemek.append(elem3)
    elem4 = browser.find_element_by_id('element4')
    elemek.append(elem4)
    elem5 = browser.find_element_by_id('element5')
    elemek.append(elem5)

    for i in elemek:
        if i.tag_name == "button":
            i.click()
            clicked = i.get_attribute('onclick')

            break


    result = browser.find_element_by_id('result')
    print(result.text)
    szoveg = result.text
    clickw = clicked[8:-2]
    print(clickw)

    if szoveg == clickw:
        print("A szöveg megegyezik")
    elif szoveg != clickw:
        print("Fail")
    else:
        print("Nincs ilyen gomb")


finally:
    browser.quit()

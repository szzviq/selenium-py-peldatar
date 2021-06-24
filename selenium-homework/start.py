from selenium import webdriver

browser = webdriver.Chrome()
URL = "https://techstepacademy.com/trial-of-the-stones"

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(URL)
browser.quit()
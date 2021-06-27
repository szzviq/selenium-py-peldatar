from selenium import webdriver

def id_kereses(element_id):
  try:
    id_search = browser.find_element_by_id(element_id)
    print(id_search)
  except:
    print("Az id nem létezik")

PATH = "C:\\Windows\\chromedriver.exe"

browser = webdriver.Chrome(PATH)
URL = "https://duckduckgo.com/?q=duck&t=h_&ia=web"

browser = webdriver.Chrome(PATH)
browser.maximize_window()
browser.get(URL)

id_kereses("nemletezik")
browser.close()
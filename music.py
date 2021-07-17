from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver


question = input("Wanna listen some tunes? (1 = Yes , 2 = No)  > ")
if question == "1":

    path = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(path)

    driver.get("https://www.youtube.com/")

    search = driver.find_element_by_name("search_query")
    search.clear()
    search.send_keys("Human")
    result = search.send_keys(Keys.ENTER)

    time.sleep(5)
    link = driver.find_element_by_link_text("Rag'n'Bone Man - Human (Official Video)")
    link.click()
elif question == "2":
    print("ok :|")

else:
    print("Invalid Input")

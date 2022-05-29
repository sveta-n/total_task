import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s = Service('chromedriver.exe')
drv = webdriver.Chrome(service=s)
try:
    drv.maximize_window()
    drv.get('http://google.com/ncr')
    time.sleep(1)
    search = drv.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    search.send_keys("selenide")
    time.sleep(1)
    search.send_keys(Keys.ENTER)
    time.sleep(1)
    element = drv.find_element(by=By.XPATH, value="//*[contains(text(), 'selenide.org')]")
    time.sleep(1)
    drv.find_element(by=By.LINK_TEXT, value='Images').click()
    element_img = drv.find_element(by=By.XPATH, value="//*[contains(text(), 'selenide')]")
    drv.find_elements()
    time.sleep(1)
    drv.find_element(by=By.LINK_TEXT, value='Все').click()

    time.sleep(1)
finally:
    drv.close()

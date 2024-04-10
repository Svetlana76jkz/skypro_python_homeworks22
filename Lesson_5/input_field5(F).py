from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Запустить сайт
driver.get("http://the-internet.herokuapp.com/inputs")

# Ввод значения "1000" в поле ввода
search_field = "[type=number]"
search_input = driver.find_element(By.CSS_SELECTOR, search_field).click()
sleep(2)
search_input.send_keys("1000")
sleep(2)
search_input.clear()
sleep(2)
search_input.send_keys("999")

sleep(10)
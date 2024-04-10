from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Запустить сайт
driver.get(" http://the-internet.herokuapp.com/login")

# В поле username введите значение tomsmith
username = "#username"
username_input = driver.find_element(By.CSS_SELECTOR, username).click()
sleep(2)
username_input.send_keys("tomsmith")
sleep(2)

# В поле password введите значение SuperSecretPassword
password = "#password"
password_input = driver.find_element(By.CSS_SELECTOR, password).click()
sleep(2)
password_input.send_keys("SuperSecretPassword")
sleep(2)

# Нажмите кнопку Login
button = driver.find_element(By.CSS_SELECTOR, "button.radius").click()

sleep(10)

# Закрыть браузер
driver.quit()
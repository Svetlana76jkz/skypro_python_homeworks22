from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


# Запустить сайт
driver.get("http://uitestingplayground.com/classattr/")

# найти синюю кнопку по CSS-классу и кликнем на нее
blue_button = driver.find_element(By.CSS_SELECTOR, "button[class='btn class1 btn-primary btn-test']").click()
sleep(5)

# Обработать оповещение
alert = driver.switch_to.alert
alert.accept()


#Кликнем на зеленую (отжать)
green_button = driver.find_element(By.CSS_SELECTOR, "button[class='btn class2 btn-success btn-test']").click()
sleep(5)

# Повторить действия три раза
for _ in range(3):
    blue_button.click()
    alert = driver.switch_to.alert
    alert.accept()
    green_button.click()

sleep(10)

driver.quit()

sleep(10)

driver.quit()

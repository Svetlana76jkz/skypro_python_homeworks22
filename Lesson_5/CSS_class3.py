from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


# Запустить сайт
driver.get("http://uitestingplayground.com/classattr/")
sleep(5)

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

from time import sleep
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(20)
driver.get("http://www.uitestingplayground.com/ajax")# Перейдите на страницу

driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()# Нажмите на синюю кнопку.

content = driver.find_element(By.CSS_SELECTOR, "#content")# Получить текст из зелёной плашки
txt = content.find_element(By.CSS_SELECTOR, "p.bg-success").text

print(txt) #вывести в консоль

driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get(" http://uitestingplayground.com/textinput") # Перейдите на страницу

input_field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")#Указать в поле ввода текст SkyPro
input_field.send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()# Нажать на синюю кнопку

button_text = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-primary")) # Получить текст кнопки
).text

print(button_text) # Вывести в консоль (SkyPro)

driver.quit()
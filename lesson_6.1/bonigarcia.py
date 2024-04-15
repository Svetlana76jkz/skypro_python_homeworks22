from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(30)
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")# Перейдите на страницу

input_name = driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]')
input_name.send_keys("Иван")

input_lastName = driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]')
input_lastName.send_keys("Петров")

input_address = driver.find_element(By.CSS_SELECTOR, 'input[name="address"]')
input_address.send_keys("Ленина, 55-3")

input_email = driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]')
input_email.send_keys("test@skypro.com")

input_phone = driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]')
input_phone.send_keys("+7985899998787")

input_city = driver.find_element(By.CSS_SELECTOR, 'input[name="city"]')
input_city.send_keys("Москва")

input_country = driver.find_element(By.CSS_SELECTOR, 'input[name="country"]')
input_country.send_keys("Россия")

input_job_position = driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]')
input_job_position.send_keys("QA")

input_company = driver.find_element(By.CSS_SELECTOR, 'input[name="company"]')
input_company.send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

sleep(30)
driver.quit()
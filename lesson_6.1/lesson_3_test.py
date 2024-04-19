from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))


def test_form_internet_mag():
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(10)
    driver.maximize_window()
    # Авторизация
    driver.find_element(By.CSS_SELECTOR, 'input[name="user-name"]').send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys("secret_sause")
    driver.find_element(By.CSS_SELECTOR, 'input[name="login-button"]').click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.CSS_SELECTOR, 'a[data-test="shopping-cart-link"]').click()
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()
    driver.find_element(By.CSS_SELECTOR, 'input[name="firstName"]').send_keys("Svetlana")
    driver.find_element(By.CSS_SELECTOR, 'input[name="lastName"]').send_keys("Voroshilova")
    driver.find_element(By.CSS_SELECTOR, 'input[name="postalCode"]').send_keys("420105")
    driver.find_element(By.CSS_SELECTOR, 'input[name="continue"]').click()
    txt = WebDriverWait(driver, "10").until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.summary_total_label'))).text
    driver.find_element(By.CSS_SELECTOR, 'button[name="finish"]').click()
    #  Закрытие браузера
    driver.quit()
    assert txt == "Total:$58.29"
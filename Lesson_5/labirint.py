from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

#зайти в labirint.ru
driver.get("https://www.labirint.ru/")

#Найти книгу по слову Python
search_field = "#search-field"
search_input = driver.find_element(By.CSS_SELECTOR, search_field)
search_input.send_keys("Python")
search_input.send_keys(Keys.ENTER)

#Сбор всех карточек товаров
books = driver.find_elements(By.CSS_SELECTOR, "div.product-card")

print(len(books))

#Вывод информации по каждой книге
for book in books:
	title = book.find_element(By.CSS_SELECTOR, "a.product-card__name").text
	price = book.find_element(By.CSS_SELECTOR, "div.product-card__price-current").text
	author = " "
	try:
		author = book.find_element(By.CSS_SELECTOR, "div.product-card__author").text
	except:
		author = "Автор не указан"	

	print(author + "\t" + title + "\t" + price)

sleep (5)
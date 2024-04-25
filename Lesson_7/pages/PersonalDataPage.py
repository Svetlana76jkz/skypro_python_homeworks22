from selenium.webdriver.common.by import By


class PersonalDataPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def personal_data(self, name, last, address, email, phone, city, country, job, company):
        self.driver.find_element(By.CSS_SELECTOR, 'input[name = "first-name"]').send_keys(name)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name = "last-name"]').send_keys(last)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name = "address"]').send_keys(address)
        self.driver.find_element(By.CSS_SELECTOR,'input[name = "e-mail"]').send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name = "phone"]').send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name = "zip-code"]').clear()
        self.driver.find_element(By.CSS_SELECTOR, 'input[name = "city"]').send_keys(city)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name = "country"]').send_keys(country)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name = "job-position"]').send_keys(job)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name = "company"]').send_keys(company)
        self.driver.find_element(By.CSS_SELECTOR, 'button').click()

    def zip_code_red(self):
        zip_code_color = self.driver.find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property("background-color")
        return zip_code_color == 'rgba(248, 215, 218, 1)'

    def other_fields_green(self):
        other_fields = ["#first-name", "#last-name", "#address", "#e-mail",
                        "#phone", "#city", "#country", "#job-position", "#company"]
        for field in other_fields:
            field_color = self.driver.find_element(By.CSS_SELECTOR, field).value_of_css_property("background-color")
        return field_color == 'rgba(209, 231, 221, 1)'

    def close_driver(self):
        self.driver.quit()

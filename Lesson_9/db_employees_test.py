import requests
import random
from faker import Faker
from EmployeesApi import EmployeesApi
from EmployeesTable import EmployeesTable

api = EmployeesApi("https://x-clients-be.onrender.com")
db = EmployeesTable("postgres://x_clients_user:x7ngHjC1h08a85bELNifgKmqZa8KIR40@dpg-cn1542en7f5s73fdrigg-a.frankfurt-postgres.render.com/x_clients_xxet")

fake = Faker()

def generate_random_employee_data():
    firstName = fake.first_name()
    lastName = fake.last_name()
    middleName = fake.middle_name()
    email = fake.email()
    url = fake.url()
    phone = fake.phone_number()
    birthdate = fake.date_of_birth(minimum_age=18,maximum_age=65)
    isActive = random.choices([True, False])
    return firstName, lastName, middleName, email, url, phone, birthdate, isActive

def test_add_new_employee():
    # Создать новую компанию
    name = "ИП Снежок"
    descr = "игрушки"
    db.create_company_db(name)
    max_id = db.get_max_id()
   
    new_company = api.get_company(max_id)
    companyId = new_company["id"]
   
    api_result_before = api.get_employees_list(companyId)
    db_result_before = db.get_emploees_db()
    assert len(api_result) == len(db_result)
    # добавить нового сотрудника
    firstName, lastName, middleName, email, url, phone, birthdate, isActive = generate_random_employee_data()
    db.create_employee_db(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)

    max_emp_id = db.get_max_id_employee()

    api_result_after = api.get_employees_list(companyId)
    db_result_after = db.get_emploees_db()

    new_employee = api.get_employee(max_emp_id)

    db.delete(max_id)

    assert  len(api_result_before) + 1 == len(api_result_after)
    assert len(db_result_before) + 1 == len(db_result_after)
    assert len(api_result_after) == len(db_result_after)
    assert new_employee [-1]["firstName"] == first_name
    assert new_employee [-1]["lastName"] == last_name
    assert new_employee [-1]["middleName"] == middle_name
    assert new_employee [-1]["companyId"] == companyId
    assert new_employee [-1]["phone"] == phone_number
    assert new_employee [-1]["birthdate"] == date_of_birth
    assert new_employee [-1]["isActive"] == True
    assert new_employee [-1]["id"] == max_emp_id

def test_get_employees_id():
    #Создать новую компанию
    name = "ООО Иванов"
    description = "перевозки"
    db.create_company_db(name)
    max_id = db.get_max_id()
   
    new_company = api.get_company(max_id)
    companyId = new_company['id']
    # добавить нового сотрудника
    firstName, lastName, middleName, email, url, phone, birthdate, isActive = generate_random_employee_data()
    db.create_employee_db(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    max_emp_id = db.get_max_id_employee()
    
    new_employee = api.get_employee(max_emp_id)
    employee_id = new_employee["id"]

    db.delete(max_id)

    assert len(api_result) == len(db_result) 
    assert new_employee[-1]["firstName"] == first_name
    assert new_employee[-1]["lastName"] ==  last_name
    assert new_employee[-1]["middleName"] == middle_name
    assert new_employee[-1]["companyId"] == companyId
    assert new_employee[-1]["phone"] ==  phone_number
    assert new_employee[-1]["birthdate"] == date_of_birth
    assert new_employee[-1]["isActive"] == True
    assert new_employee[-1]["id"] == max_emp_id

def test_patch_employee():
    #Создать новую компанию
    name = "ИП Машинист"
    descr = "перевозки"
    db.create_company_db(name)
    max_id = db.get_max_id()
  
    new_company = api.get_company(max_id)
    companyId = new_company["id"]
    # добавить нового сотрудника
    firstName, lastName, middleName, email, url, phone, birthdate, isActive = generate_random_employee_data()
    db.create_employee_db(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    max_emp_id = db.get_max_id_employee()

    new_employee = api.get_employee(max_emp_id)
    employee_id = new_employee["id"]
    # Изменить информацию по сотруднику
    new_lastName = "Petrov"
    new_email = "bzreva123@mail.ru"
    new_url = "_Updated_"
    new_phone = "Updated"
    new_isActive = False
    edited = api.edit_employee(employee_id, new_lastName, new_email, new_url, new_phone, new_isActive)

    db.delete(max_id)
    
    assert len(api_result) == len(db_result) 
    assert edited["email"] == "bzreva123@mail.ru"
    assert edited["url"] == "_Updated_"
    assert edited["isActive"] == False    
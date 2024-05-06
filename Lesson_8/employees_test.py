import requests
from CompanyApi import CompanyApi

api = CompanyApi("https://x-clients-be.onrender.com")

                                                                                                                                                

def test_add_new_employee():
    #Создать новую компанию
    name = "DONOR"
    descr = "magazin books"
    result = api.create_company(name, descr)
    new_id = result["id"]
    #Обращаемся к компании
    new_company = api.get_company(new_id)
    company_id = new_company['id']
    # получить список сотруднико до...
    body = api.get_employees_list(companyId=company_id)
    len_before = len(body)
     # добавить нового сотрудника
    firstName = "svetlana"
    lastName = "voroshilova"
    middleName = "aleksandrovna"
    companyId = new_company
    email = "voroshilova123@mail.ru"
    url = "string"
    phone = "865423175266"
    birthdate = "2024-05-06T11:16:51.864Z"
    isActive = True
    result = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    emp_id = result["id"]
    # получить список сотрудников новой компании после....
    body = api.get_employees_list(companyId=company_id) 
    len_after = len(body)
    assert len_after - len_before == 1
    assert body[-1]["firstName"] == "svetlana"
    assert body[-1]["lastName"] == "voroshilova"
    assert body[-1]["middleName"] == "aleksandrovna"
    assert body[-1]["companyId"] == new_company
    assert body[-1]["email"] == "voroshilova123@mail.ru"
    assert body[-1]["url"] == "string"
    assert body[-1]["phone"] == "865423175266"
    assert body[-1]["birthdate"] == "2024-05-06T11:16:51.864Z"
    assert body[-1]["isActive"] == True
    assert body[-1]["id"] == emp_id

def test_get_employees_id():
    #Создать новую компанию
    name = "ООО Иванов"
    descr = "перевозки"
    new_company = api.create_company(name, descr)
    new_id = new_company["id"]
    #Обращаемся к компании
    new_company = api.get_company(new_id)
    company_id = new_company['id']
    # добавить нового сотрудника
    firstName = "olga"
    lastName = "petrova"
    middleName = "alekseevna"
    companyId = company_id
    email = "petrova123@mail.ru"
    url = "string"
    phone = "865423175123"
    birthdate = "2001-05-06T11:16:51.864Z"
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    emp_id = new_employee["id"]
    # получить список сотрудников новой компании после....
    body = api.get_employees_list(companyId=company_id) 
    #Обращаемся к сотруднику по ID
    new_employee = api.get_employee(emp_id)
    employee_id = new_employee['id']
    assert body[-1]["firstName"] == "olga"
    assert body[-1]["lastName"] ==  "petrova"
    assert body[-1]["middleName"] == "alekseevna"
    assert body[-1]["companyId"] == new_company
    assert body[-1]["email"] == "petrova123@mail.ru"
    assert body[-1]["url"] == "string"
    assert body[-1]["phone"] ==  "865423175123"
    assert body[-1]["birthdate"] == "2001-05-06T11:16:51.864Z"
    assert body[-1]["isActive"] == True
    assert new_employee["id"] == emp_id

def test_patch_employee():
    #Создать новую компанию
    name = "ИП Машинист"
    descr = "перевозки"
    new_company = api.create_company(name, descr)
    new_id = new_company["id"]
    #Обращаемся к компании
    new_company = api.get_company(new_id)
    company_id = new_company['id']
    # добавить нового сотрудника
    firstName = "Ирина"
    lastName = "Лазарева"
    middleName = "Владимировна"
    companyId = company_id
    email = "lazareva123@mail.ru"
    url = "string"
    phone = "865423175456"
    birthdate = "2006-05-06T11:16:51.864Z"
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    emp_id = new_employee["id"]
    # получить список сотрудников новой компании после....
    body = api.get_employees_list(companyId=company_id) 
    #Обращаемся к сотруднику по ID
    new_employee = api.get_employee(emp_id)
    employee_id = new_employee['id']
    # Изменить информацию по сотруднику
    new_firstName = "Updated"
    new_lastName = "Updated"
    new_email = "Updated"
    new_url = "Updated"
    new_phone = "Updated"
    new_isActive = "Updated"
    edited = api.edit_employee( new_firstName, new_lastName, new_email, new_url, new_phone, new_isActive)
    assert edited["id"] == new_id
    assert edited["firstName"] == new_firstName
    assert edited["lastName"] == new_lastName
    assert edited["email"] == new_email
    assert edited["url"] == new_url
    assert edited["lastphone"] == new_phone
    assert edited["isActive"] == True
    


    
    
   



    
   
   
  
   
   




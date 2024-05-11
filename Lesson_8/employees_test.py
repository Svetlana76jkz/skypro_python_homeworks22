import requests
from EmployeesApi import EmployeesApi

api = EmployeesApi("https://x-clients-be.onrender.com")

def test_add_new_employee():
      #Создать новую компанию
    name = "DONOR"
    descr = "magazin books"
    result = api.create_company(name, descr)
    new_id = result["id"]
    #Обращаемся к компании
    new_company = api.get_company(new_id)
    companyId = new_company["id"]
    # получить список сотруднико до...
    body = api.get_employees_list(companyId)
    len_before = len(body)
     # добавить нового сотрудника
    firstName = "svetlana"
    lastName = "voroshilova"
    middleName = "aleksandrovna"
    company = companyId
    email = "voroshilova123@mail.ru"
    url = "string"
    phone = "865423175266"
    birthdate = "2024-05-06T11:16:51.864Z"
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    emp_id = new_employee["id"]
    # получить список сотрудников новой компании после....
    body = api.get_employees_list(companyId) 
    len_after = len(body)
    assert len_after - len_before == 1
    assert body[-1]["firstName"] == "svetlana"
    assert body[-1]["lastName"] == "voroshilova"
    assert body[-1]["middleName"] == "aleksandrovna"
    assert body[-1]["companyId"] == companyId
    assert body[-1]["phone"] == "865423175266"
    assert body[-1]["birthdate"] == "2024-05-06"
    assert body[-1]["isActive"] == True
    assert body[-1]["id"] == emp_id

def test_get_employees_id():
    #Создать новую компанию
    name = "ООО Иванов"
    descr = "перевозки"
    new_company = api.create_company(name, descr)
    new_id = new_company["id"]
    #Обращаемся к компании по ID
    new_company = api.get_company(new_id)
    companyId = new_company['id']
    # получить список сотрудников новой компании до....
    body = api.get_employees_list(companyId)
    begin_list = len(body) 
    # добавить нового сотрудника
    firstName = "olga"
    lastName = "voronina"
    middleName = "alekseevna"
    company = companyId
    email = "voronina123@mail.ru"
    url = "string"
    phone = "865423175456"
    birthdate = "2001-05-06T11:16:51.864Z"
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    emp_id = new_employee["id"]
    # получить список сотрудников новой компании после....
    body = api.get_employees_list(companyId)
    after_list = len(body)
    assert after_list - begin_list == 1
    #Обращаемся к сотруднику по ID
    new_employee = api.get_employee(emp_id)
    employee_id = new_employee["id"]
    assert body[-1]["firstName"] == "olga"
    assert body[-1]["lastName"] ==  "voronina"
    assert body[-1]["middleName"] == "alekseevna"
    assert body[-1]["companyId"] == companyId
    assert body[-1]["phone"] ==  "865423175456"
    assert body[-1]["birthdate"] == "2001-05-06"
    assert body[-1]["isActive"] == True
    assert body[-1]["id"] == emp_id

def test_patch_employee():
    #Создать новую компанию
    name = "ИП Машинист"
    descr = "перевозки"
    new_company = api.create_company(name, descr)
    new_id = new_company["id"]
    #Обращаемся к компании
    new_company = api.get_company(new_id)
    companyId = new_company["id"]
    # добавить нового сотрудника
    firstName = "irina"
    lastName = "Базарева"
    middleName = "alekseevna"
    company = companyId
    email = "bazareva123@mail.ru"
    url = "string"
    phone = "865423175456"
    birthdate = "2001-05-06"
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    emp_id = new_employee["id"]
    # получить список сотрудников новой компании после....
    body = api.get_employees_list(companyId) 
    #Обращаемся к сотруднику по ID
    new_employee = api.get_employee(emp_id)
    employee_id = new_employee["id"]
    # Изменить информацию по сотруднику
    new_lastName = "Козин"
    new_email = "bzreva123@mail.ru"
    new_url = "_Updated_"
    new_phone = "Updated"
    new_isActive = False
    edited = api.edit_employee(employee_id, new_lastName, new_email, new_url, new_phone, new_isActive)
    assert edited["lastName"] == "Козин"
    assert edited["email"] == "bzreva123@mail.ru"
    assert edited["url"] == "_Updated_"
    assert edited["phone"] == "Updated"
    assert edited["isActive"] == False

    
    
   



    
   
   
  
   
   




import requests
from EmployeesApi import EmployeesApi
from EmployeesTable import EmployeesTable

api = EmployeesApi("https://x-clients-be.onrender.com")
db = EmployeesTable("postgres://x_clients_user:x7ngHjC1h08a85bELNifgKmqZa8KIR40@dpg-cn1542en7f5s73fdrigg-a.frankfurt-postgres.render.com/x_clients_xxet")

def test_add_new_employee():
    # Создать новую компанию
    name = 'DONOR'
    description = "сдача крови"
    db.create_company_db(name)
    max_id = db.get_max_id()
    #Обращаемся к компании по ID
    new_company = api.get_company(max_id)
    companyId = new_company["id"]
     # получить список сотрудников новой компании до....
    api_result = api.get_employees_list(companyId)
    db_result = db.get_emploees_db()
    assert len(api_result) == len(db_result)
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
    db.create_employee_db(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    max_emp_id = db.get_max_id_employee()
    # получить список сотрудников новой компании после....
    api_result = api.get_employees_list(companyId)
    db_result = db.get_emploees_db()
    db.delete(max_id)
    assert  len(api_result) == len(db_result)
    assert body[-1]["firstName"] == "svetlana"
    assert body[-1]["lastName"] == "voroshilova"
    assert body[-1]["middleName"] == "aleksandrovna"
    assert body[-1]["companyId"] == companyId
    assert body[-1]["phone"] == "865423175266"
    assert body[-1]["birthdate"] == "2024-05-06"
    assert body[-1]["isActive"] == True
    assert body[-1]["id"] == max_emp_id
    
def test_get_employees_id():
    #Создать новую компанию
    name = "ООО Иванов"
    description = "перевозки"
    db.create_company_db(name)
    max_id = db.get_max_id()
    #Обращаемся к компании по ID
    new_company = api.get_company(max_id)
    companyId = new_company['id']
    # получить список сотрудников новой компании до....
    api_result = api.get_employees_list(companyId)
    db_result = db.get_emploees_db()
    assert len(api_result) == len(db_result) 
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
    db.create_employee_db(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    max_emp_id = db.get_max_id_employee()
    # получить список сотрудников новой компании после....
    api_result = api.get_employees_list(companyId)
    db_result = db.get_emploees_db()
    #Обращаемся к сотруднику по ID
    new_employee = api.get_employee(max_emp_id)
    employee_id = new_employee["id"]
    db.delete(max_id)
    assert len(api_result) == len(db_result) 
    assert body[-1]["firstName"] == "olga"
    assert body[-1]["lastName"] ==  "voronina"
    assert body[-1]["middleName"] == "alekseevna"
    assert body[-1]["companyId"] == companyId
    assert body[-1]["phone"] ==  "865423175456"
    assert body[-1]["birthdate"] == "2001-05-06"
    assert body[-1]["isActive"] == True
    assert body[-1]["id"] == max_emp_id

def test_patch_employee():
    #Создать новую компанию
    name = "ИП Машинист"
    descr = "перевозки"
    db.create_company_db(name)
    max_id = db.get_max_id()
    #Обращаемся к компании
    new_company = api.get_company(max_id)
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
    db.create_employee_db(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    max_emp_id = db.get_max_id_employee()
    # получить список сотрудников новой компании после....
    api_result = api.get_employees_list(companyId)
    db_result = db.get_emploees_db()
    #Обращаемся к сотруднику по ID
    new_employee = api.get_employee(max_emp_id)
    employee_id = new_employee["id"]
    # Изменить информацию по сотруднику
    new_lastName = "Козин"
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
    
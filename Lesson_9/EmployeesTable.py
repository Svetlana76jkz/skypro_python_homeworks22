from sqlalchemy import create_engine
from sqlalchemy.sql import text

class EmployeesTable:
    self.__scripts = {
        "select": text("select * from employee where company_id = : companyId"),
        "delete by id": text("delete from employee where id = : id_to_delete"),
        "insert new company": text("insert into company (name, description) values (:new_name, :new_description)"),
        "get max id company": text("select MAX(id) from company"),
        "insert new employee": text("insert into employee (id, first_name, last_name, middle_name, company_id, email, avatar_url, phone, birthdate, is_active) values (:new_id, :new_firstName, :new_lastName, :new_middleName, :new_companyId, :new_email, :new_url, :new_phone, :new_birthdate, :new_isActive)"),
        "get max id employee": text("select MAX(id) from employee")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_emploees_db(self):
        return self.__db.execute(self.__scripts["select"]).fetchall()

    def delete(self, id):
        self.__db.execute(self.__scripts["delete by id"], id_to_delete = id)

    def create_company_db(self, name, description):
        self.__db.execute(self.__scripts["insert new company"], new_name = name, new_description = description)

    def get_max_id(self):
        return self.__db.execute(self.__scripts["get max id company"]).fetchall()[0][0]

    def create_employee_db(self, firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive):
        self.__db.execute(self.__scripts["insert new employee"], new_firstName = firstName, new_lastName = lastName, new_middleName = middleName, new_companyId = companyId, new_email = email, new_url = url, new_phone = phone, new_birthdate = birthdate, new_isActive = isActive)

    def get_max_id_employee(self):
        return self.__db.execute(self.__scripts["get max id employee"]).fetchall()[0][0]
from sqlalchemy import create_engine
from sqlalchemy.sql import text

class EmployeesTable:
    __scripts = {
        "select": "select name from employees where company = : companyId",
        "delete by id": text("delete from company where id = : id_to_delete"),
        "insert new company": txt("insert into company (\"name\", \"description\") values (:new_name, description)"),
        "get max id": "select MAX(\"id\") from company where deleted _at is null",
        "insert new employee": txt("insert into employees (\"firstName\", \"lastName\", \"middleName\", \"companyId\", \"email\", \"url\", \"phone\", \"birthdate\", \"isActive\") values (: new_firstName, new_lastName, new_middleName, new_companyId, new_email, new_url, new_phone, new_birthdate, new_isActive)"),
        "get max id employee": "select MAX(\"id\" AS max_employee_id from employees where company_id = (select MAX(\"id\") from company where deleted _at is null))"
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_emploees_db(self,):
        return self.__db.execute(self.__scripts["select"]).fetchall()

    def delete(self, id):
        self.__db.execute(self.__scripts["delete by id"], id_to_delete = id)

    def create_company_db(self, name, description):
        self.__db.execute(self.__scripts["insert new company"], new_name = name, new_description = description)

    def get_max_id(self):
        return self.__db.execute(self.__scripts["get max id"]).fetchall()[0][0]

    def create_employee_db(self, firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive):
        self.__db.execute(self.__scripts["insert new employee"], new_firstName = firstName, new_lastName = lastName, new_middleName = middleName, new_companyId = companyId, new_email = email, new_url = url, new_phone = phone, new_birthdate = birthdate, new_isActive = isActive)

    def get_max_id_employee(self):
        return self.__db.execute(self.__scripts["get max id employee"]).fetchall()[0][0]

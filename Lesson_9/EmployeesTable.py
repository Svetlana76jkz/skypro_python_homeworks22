from sqlalchemy import create_engine
from sqlalchemy.sql import text

class EmployeesTable:
    self.__scripts = {
       "insert new company": text("insert into company (name, description) values (:new_name, :new_description)"),
        "get max id company": text("select MAX(id) AS max_id from company"),
        "select": text("select * from employee where id = : companyId"),
        "insert new employee": text("insert into employee (first_name, last_name, middle_name, phone, email, birthdate, avatar_url, company_id) values (:new_firstName, :new_lastName, :new_middleName, :new_companyId, :new_email, :new_url, :new_phone, :new_birthdate, :new_isActive)"),
        "get max id empl": text("select MAX(id) AS max_id from employee"),
        "edited employee": text("update employee set last_name = :new_lastName, email = :new_email, url = :new_url, phone = :new_phone, isActive = :new_isActive where id = :employeeId"),
        "delete id employee": text("delete from employee where id = : id_to_delete"),
        "delete by id": text("delete from company where id = : id_to_delete")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def create_company_db(self, name, description):
        return self.__db.execute(self.__scripts["insert new company"], new_name = name, new_description = description)

    def get_max_id_company(self):
        return self.__db.execute(self.__scripts["get max id company"]).fetchall()[0][0]

    def delete(self, id):
        return self.__db.execute(self.__scripts["delete by id"], id_to_delete = id)     

    def get_emploees_db(self):
        return self.__db.execute(self.__scripts["select"]).fetchall()    

    def create_employee_db(self, firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive):
        return self.__db.execute(self.scripts["insert new employee"], new_firstName=firstName, new_lastName=lastName, new_middleName=middleName, new_companyId=companyId, new_email=email, new_url=url, new_phone=phone, new_birthdate=birthdate, new_isActive=isActive)

    def get_max_id_employee(self):
        return self.__db.execute(self.__scripts["get max id empl"]).fetchall()[0][0]

    def update_employee(self, employeeId, new_lastName, new_email, new_url, new_phone, new_isActive):
        return self.__db.execute(self.scripts["edited employee"], employeeId=employeeId, new_lastName=new_lastName, new_email=new_email, new_url=new_url, new_phone=new_phone, new_isActive=new_isActive)

    def delete_employee_db():
         return self.__db.execute(self.__scripts["delete id employee"], id_to_delete = id)

        


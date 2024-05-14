db = create_engine(db_connection_string)

# получить список таблиц
def test_db_connection():
    db = create_engine(db_connection_string)
    names = db.table_names()
    assert names[0] == 'company'

# получить строки из таблицы
def test_select():
    db = create_engine(db_connection_string)
    rows = db.execute("select * from company").fetchall()
    row1 = rows(0)

    assert row1[-1] == 1468
    assert row1["name"] == "hgfdtdm"

# получить строки по 1 фильтру
def test_select_1_row():
    db = create_engine(db_connection_string)
    sql_statement = text("select * from company where id = :company_id")
    rows = db.execute(sql_statement, company_id = 112).fetchall()

    assert len(rows) == 1
    assert rows[0]["name"] == "Кондитерская Профитроли"

# получить строки по 2м фильтрам (1 способ)
def test_select_2_row():
    db = create_engine(db_connection_string)
    sql_statement = text("select * from company where \"isActive\" = :isActive and id >= :id")
    rows = db.execute(sql_statement, id = 113, isActive = True).fetchall()

    assert len(rows) == 2

# получить строки по 2м фильтрам (2 способ)
def test_select_2_row():
    db = create_engine(db_connection_string)
    sql_statement = text("select * from company where \"isActive\" = :isActive and id >= :id")

    my_params = {
        'id': 1468,
        'is_active': True
    }

    rows = db.execute(sql_statement, my_params).fetchall()

    assert len(rows) == 2

# добавить компанию insert
def test_insert():
    db = create_engine(db_connection_string)
    sql = txt("insert into company (\"name\") values (:new_name)")
    rows = db.execute(sql, new_name = 'SkyPro')

# Обновить компанию. update
def test_update():
    db = create_engine(db_connection_string)
    sql = text("update company set description = :descr where id = :id")
    rows = db.execute(sql, descr = 'New descr', id = 1704)

# Удалить компанию. delete
def test_delete():
    db = create_engine(db_connection_string)
    sql = text("delete from company where id = :id")
    rows = db.execute(sql, id = 1704)
 

# select name from employees where company = 'название_компании'
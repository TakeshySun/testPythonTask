import sqlite3
from realization.zip import myDict


"""Надо изменить conn (на папку в которую мы хотим сохранить *.db файл)"""
conn = sqlite3.connect('D:/testPythonTask/for_test3.db')
cursor = conn.cursor()

# Создание таблицы
cursor.execute("CREATE TABLE IF NOT EXISTS sum (object_id VARCHAR(32), object_type varchar(8), cost FLOAT)")

#Var_1 gde dybliruem Kod
# cursor.executemany("INSERT INTO sum (object_id, object_type, cost) VALUES (?, 'env', ?)", myDict['env_id'].items())

# Var_2
# for obj_type, results in myDict.items():
#     cursor.executemany("INSERT INTO sum (object_id, object_type, cost) VALUES (?, '%s', ?)" % obj_type, results.items())


# Var_3 S generatorom
for obj_type, results in myDict.items():
    cursor.executemany(
        "insert into sum (object_id, object_type, cost) VALUES (?, ?, ?);",
        ((obj_id, obj_type, obj_cost) for obj_id, obj_cost in results.items()))


conn.commit()


cursor.execute('SELECT * FROM sum')

meida = cursor.fetchall()

print(meida)

conn.close()
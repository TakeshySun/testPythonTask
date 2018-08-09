import sqlite3
import csv, io
import requests
from io import BytesIO
from zipfile import ZipFile


class Reader(object):
    def __init__(self, myDict):
        self.myDict = {
            "env_id": {},
            'farm_id': {},
            'farm_role_id': {},
            "server_id": {}
        }

    """ Kод, читает из урлы потом читает зип,"""

    def url_read(self, zip_file, files):
        response = requests.get(
            "https://s3.amazonaws.com/detailed-billing-test/615271354814-aws-billing-detailed-line-items-with-resources-and-tags-2016-05.csv.zip")
        zip_file = ZipFile(BytesIO(response.content))
        files = zip_file.namelist()

    def wrote_dict(self):
        with zip_file.open(files[0]) as csvfile:
            file = io.TextIOWrapper(csvfile, encoding="utf-8")

            for row in csv.DictReader(file):
                scalr_meta = row['user:scalr-meta']
                cost = float(row['Cost'])
                mylist = scalr_meta.split(':')

                # Skip empty Scalr-meta row
                if not scalr_meta:
                    continue
                """Читаем по индексу для четырех object_type и делаем сумму cost. Все данные помещаем в myDict"""
                if not mylist[1]:
                    continue
                if mylist[1] in myDict['env_id']:
                    myDict['env_id'][mylist[1]] += cost
                else:
                    myDict['env_id'][mylist[1]] = cost

                if not mylist[2]:
                    continue
                if mylist[2] in myDict['farm_id']:
                    myDict['farm_id'][mylist[2]] += cost
                else:
                    myDict['farm_id'][mylist[2]] = cost

                if not mylist[3]:
                    continue
                if mylist[3] in myDict['farm_role_id']:
                    myDict['farm_role_id'][mylist[3]] += cost
                else:
                    myDict['farm_role_id'][mylist[3]] = cost

                if not mylist[4]:
                    continue
                if mylist[4] in myDict['server_id']:
                    myDict['server_id'][mylist[4]] += cost
                else:
                    myDict['server_id'][mylist[4]] = cost



class SqlWrote(object):
    def __init__(self):
        self.db_path = './testPythonTask/for_test.db'

    @property
    def connection(self):

        """Надо изменить conn (на папку в которую мы хотим сохранить *.db файл)"""
        conn = sqlite3.connect('./testPythonTask/for_test3.db')
        cursor = conn.cursor()
        return conn

    def create_table(self):
        # Создание таблицы
        cursor.execute("CREATE TABLE IF NOT EXISTS sum (object_id VARCHAR(32), object_type varchar(8), cost FLOAT)")

    def wrote_in_db(self):

        for obj_type, results in myDict.items():
            cursor.executemany(
                "insert into sum (object_id, object_type, cost) VALUES (?, ?, ?);",
                ((obj_id, obj_type, obj_cost) for obj_id, obj_cost in results.items()))


            conn.commit()

            cursor.execute('SELECT * FROM sum')

            meida = cursor.fetchall()

            print(meida)

            conn.close()
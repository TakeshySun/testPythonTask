import csv, io, sys, zipfile, os


import pandas as pd
import requests
from io import BytesIO, StringIO
from zipfile import ZipFile




myDict = {
    "env_id": {},
    'farm_id': {},
    'farm_role_id': {},
    "server_id": {}
}
""" Kод, читает из урлы потом читает зип,"""
response = requests.get('https://s3.amazonaws.com/detailed-billing-test/615271354814-aws-billing-detailed-line-items-with-resources-and-tags-2016-05.csv.zip')
zip_file = ZipFile(BytesIO(response.content))
files = zip_file.namelist()
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
        if mylist[4] in  myDict['server_id']:
            myDict['server_id'][mylist[4]] += cost
        else:
            myDict['server_id'][mylist[4]] = cost


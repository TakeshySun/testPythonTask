import csv
import sqlite3

results2 = {}
# SCALR_ENV_ID = {}
SCALR_FARM_ID = {}
SCALR_FARM_ROLE_ID = {}
SCALR_SERVER_ID = {}

myDict = {
    "env_id": {},
    'farm_id': {},
    'farm_role_id': {},
    "server_id": {}
}



with open('D:/testPythonTask/files/first-2016-05.csv', newline='') as f:
    reader = csv.DictReader(f)
    # sortedlist = sorted(reader, key=lambda row: (row['user:scalr-meta']), reverse=False)




    for row in reader:
        scalr_meta = row['user:scalr-meta']
        cost = float(row['Cost'])
        mylist = scalr_meta.split(':')


     # Skip empty Scalr-meta row
        if not scalr_meta:
            continue

        # Чисто для крсаоты посмотреть сумму по разным полным scalr.metatag
        # if scalr_meta in results2:
        #     results2[scalr_meta] += cost
        # else:
        #     results2[scalr_meta] = cost


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


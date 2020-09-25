import sqlite3
import json

"""
Populate the db.file with a sample json named `sample_data.json`
"""

with open('sample_data.json', 'r') as f:
    dict_data = json.load(f)

try:
    sqliteConnection = sqlite3.connect('db.sqlite3')
    cursor = sqliteConnection.cursor()
    print('Successfully connected to sqlite')

    sqlite_insert_query = ("""INSERT INTO api_courtdecision
    (n_processo, ementa, favor_contribuinte, id_cliente)
    VALUES
    (?, ?, ?, ?);""")
    for data in dict_data:
        data_tuple = (data['n_processo'], data['ementa'], data['favor_contribuinte'], data['id_cliente'])
        cursor.execute(sqlite_insert_query, data_tuple)
        sqliteConnection.commit()
        print('Record inserted successfully into db')
    cursor.close()
except sqlite3.Error as error:
    print('failed to insert {}'.format(error))
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print('connection closed')


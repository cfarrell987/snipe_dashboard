import psycopg2
import os
import json
import sys


def load_json():
    file = 'hardware.json'

    with open(file) as data:
        record_list = json.load(data, object_hook=list)
    if type(record_list) == list:
        first_record = record_list[0]
    # columns = list(first_record.keys())
    # print("\ncolumn names: ", columns)


def conn_database():
    conn = psycopg2.connect("dbname=dbSnipeHardware user=admin")
    cur = conn.cursor()
    cur.close()
    conn.close()

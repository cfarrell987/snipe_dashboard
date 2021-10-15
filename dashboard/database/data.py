import psycopg2
import os
import json


def conn_database():
    conn = psycopg2.connect("dbname=dbSnipeHardware user=admin")
    cur = conn.cursor()
    cur.close()
    conn.close()

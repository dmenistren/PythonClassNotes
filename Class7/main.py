import pandas as pd
import psycopg2

def db_con():
    '''
    get the connection from the DB
    '''
    con = psycopg2.connect(
        "dbname=person user=postgres password=hello123 host=localhost")
    cur = con.cursor()
    return con, cur


df = pd.read_json('test_data.json')

con , cur = db_con()
query = "INSERT INTO person (id, first_name, last_name, address, city, country) values(%s,%s,%s,%s,%s,%s)"
cur.executemany(query, df.values.tolist())
con.commit()
con.close()



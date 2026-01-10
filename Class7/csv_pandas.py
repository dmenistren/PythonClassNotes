import pandas as pd
import psycopg2


def db_conn():
    '''
    get the connection from the DB
    '''
    con = psycopg2.connect(
        "dbname=pythonclass user=postgres password=toor host=localhost")
    cur = con.cursor()
    return con, cur


df = pd.read_csv('data.csv')
df['gender'] = df['gender'].apply(lambda x: x if x.lower() in [
                                  'male', 'female'] else 'trans'.title())

con, cur = db_conn()
insert_query = """INSERT INTO users (id,first_name,last_name,email,gender,ip_address) values(%s,%s,%s,%s,%s,%s)"""
cur.executemany(insert_query, df.values.tolist())
con.commit()
con.close()

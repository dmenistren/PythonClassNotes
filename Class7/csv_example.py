import csv
import psycopg2

insert_query = """INSERT INTO users (id,first_name,last_name,email,gender,ip_address) values(%s,%s,%s,%s,%s,%s)"""


def db_conn():
    '''
    get the connection from the DB
    '''
    con = psycopg2.connect(
        "dbname=pythonclass user=postgres password=toor host=localhost")
    cur = con.cursor()
    return con, cur


con, cur = db_conn()
with open('data.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)
        gender = row['gender']
        if gender.lower() not in ['male', 'female']:
            gender = 'trans'
        cur.execute(insert_query, (row['id'], row['first_name'], row['last_name'],
                                   row['email'], gender, row['ip_address']))
        con.commit()

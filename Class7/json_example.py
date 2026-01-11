import json
import psycopg2


def db_conn():
    '''
    get the connection from the DB
    '''
    con = psycopg2.connect(
        "dbname=pythonclass user=postgres password=toor host=localhost")
    cur = con.cursor()
    return con, cur


# ETL    Extract Transform Load


data = None
# Extract
with open('data.json', 'r') as file:

    # Transform
    data = json.loads(file.read())


con, cur = db_conn()
print(con, cur)

insert_query = """INSERT INTO users (id,first_name,last_name,email,gender,ip_address) values(%s,%s,%s,%s,%s,%s)"""

for value in data:
    gender = value['gender']
    if gender.lower() not in ['male', 'female']:
        gender = 'trans'
    cur.execute(insert_query, (value['id'], value['first_name'], value['last_name'],
                               value['email'], gender, value['ip_address']))
    con.commit()

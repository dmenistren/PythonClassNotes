import psycopg2

"""
To do:
-------
1. get connection DB  -completed
2. get all the value -completed
3. I need to update the value -completed
4. need to inset the value -completed
5. need to delete value -completed
"""


def db_conn():
    '''
    get the connection from the DB
    '''
    con = psycopg2.connect(
        "dbname=pythonclass user=postgres password=toor host=localhost")
    cur = con.cursor()
    return con, cur


def get_data_db(cur):
    cur.execute("select * from person p where p.id = 12345")
    return cur.fetchall()


def update_data_db(con, cur, email, id):
    query = "update person p set email=%s where p.id = %s "
    cur.execute(query, (email, id))
    con.commit()


def delete_data_db(con, cur, id):
    query = 'delete from person where id = %s'
    cur.execute(query, (id,))
    con.commit()


def insert_data_db(con, cur, id, email, fname, lname, gender):
    query = """INSERT INTO public.person
        (id, first_name, last_name, email, gender)
        VALUES(%s, %s, %s, %s, %s);"""
    cur.execute(query, (id, fname, lname, email, gender))
    con.commit()


if __name__ == '__main__':
    print("haswe")
    con, cur = db_conn()
    update_data_db(con, cur, "demo@text.com", '54')
    insert_data_db(con, cur, "12345", "test.com", "demi", "dennis", 'male')
    delete_data_db(con, cur, 34)
    value = get_data_db(cur)
    print(value)
    con.close()

import psycopg2
def db_conn():
    """
    Get the connection from the DB
    """
    con = psycopg2.connect("dbname=user user=postgres password=hello123 host=localhost")
    cur = con.cursor()
    return con, cur


def db_get_data(cur):
    """
    get the data from the db
    """
    cur.excecute("select * from users where id =3")
    return cur.fetchall() # fetchone returns one tuple

def db_ins(con,cur, first_name, last_name, email, gender ,registration_date):
    """
    insert data in db   
    """
    query = "INSERT INTO users (id, first_name, last_name, email, gender, registration_date) VALUES(%s, %s, %s, %s, %s, %s);"
    cur.execute(query,(id, first_name, last_name, email, gender, registration_date))
    con.commit()# if we lose connection to the db all the changes will be lost


def db_upd(con, cur, id, first_name, last_name, email, gender , registration_date):
    """
    Update Data
    """
    query = "UPDATE public.users SET id=%s, first_name=%s, last_name=%s, email=%s, gender=%s, registration_date=%s;"
    cur.execute (query,(id, first_name,last_name,email,gender, registration_date))
    con.commit()

def db_del(con, cur, id ):
    """
    Delete Data
    """
    query ="DELETE FROM users WHERE id=%s ;"
    cur.execute(query(id,)) # , to make it a tuple
    con.commit()

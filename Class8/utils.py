import psycopg2


def db_conn():
    '''
    get the connection from the DB
    '''
    con = psycopg2.connect(
        "dbname=pythonclass user=postgres password=toor host=localhost")
    cur = con.cursor()
    return con, cur

### Create the virutal environment:

```python
python -m venv env
env/Scripts/activate
```

### Install python package

```python
pip install psycopg2
```

### Create a Table in PSQL

```python
CREATE TABLE public.person (
	id int4 NULL,
	first_name varchar(50) NULL,
	last_name varchar(50) NULL,
	email varchar(50) NULL,
	gender varchar(50) NULL
);
```

### Connect the python with PSQL

```python
import psycopg2

def get_db_connection():
    '''
    function to get the DB connection
    '''
    connection = psycopg2.connect(
        database='pythonclass', host='localhost', username='postgres', password='toor')
    cursor = connection.cursor()
    return connection, cursor

```

### Insert the Data in PSQL using the python

```python
def insert_data_db(connection: psycopg2.extensions.connection, cursor: psycopg2.extensions.cursor, id: int, fname: str, lname: str, email: str, gender: str):
    query = """INSERT INTO public.person
                    (id, first_name, last_name, email, gender)
                    VALUES(%s, %s, %s, %s, %s);"""
    cursor.execute(query, (id, fname, lname, email, gender))
    connection.commit()

```

### update the data in PSQL using the python

```python
def update_data_db(connection: psycopg2.extensions.connection, cursor: psycopg2.extensions.cursor, id: int, changed_email: str):
    query = "update person set email = %s where id = %s"
    cursor.execute(query, (changed_email, id))
    connection.commit()
```

### Delete the data in PSQL using the Python

```python
def delete_data_db(con, cur, id):
    query = 'delete from person where id = %s'
    cur.execute(query, (id,))
    con.commit()

```

### Select the data from the PSQL using the python

```python
def select_data_db(cur):
    query = 'select * from person p'
    cur.execute(query)
    # print(cur.fetchall())
    print(cur.fetchone())

```

### Full Code

```python
import psycopg2

def get_db_connection():
    '''
    function to get the DB connection
    '''
    connection = psycopg2.connect(
        database='pythonclass', host='localhost', user='postgres', password='toor')
    cursor = connection.cursor()
    return connection, cursor

def insert_data_db(connection: psycopg2.extensions.connection, cursor: psycopg2.extensions.cursor, id: int, fname: str, lname: str, email: str, gender: str):
    query = """INSERT INTO public.person
                    (id, first_name, last_name, email, gender)
                    VALUES(%s, %s, %s, %s, %s);"""
    cursor.execute(query, (id, fname, lname, email, gender))
    connection.commit()

def update_data_db(connection: psycopg2.extensions.connection, cursor: psycopg2.extensions.cursor, id: int, changed_email: str):
    query = "update person set email = %s where id = %s"
    cursor.execute(query, (changed_email, id))
    connection.commit()

def delete_data_db(con, cur, id):
    query = 'delete from person where id = %s'
    cur.execute(query, (id,))
    con.commit()

def select_data_db(cur):
    query = 'select * from person p'
    cur.execute(query)
    # print(cur.fetchall())
    print(cur.fetchone())

if __name__ == '__main__':
    print("Started ...")
    try:
        con = None
        con, cur = get_db_connection()
        insert_data_db(con, cur, 2, 'demo3', 'name3', 'test@demo.com', 'female')
        update_data_db(con, cur, 2, 'demo.com')
        delete_data_db(con, cur, 2)
        select_data_db(cur)
        con.close()
    except Exception as e:
        print(e)
    finally:
        if con:
            con.close()
        print("CRUD operation Completed")

```

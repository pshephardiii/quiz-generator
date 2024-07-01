from getpass import getpass
from mysql.connector import connect, Error
from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()

# Alternative way:
    # user=input("Enter username: "),
    # password=getpass("Enter password: "),

connection = connect(
    host=(os.getenv("SERVER")),
    port=(os.getenv("PORT")),
    user=(os.getenv("USERNAME")),
    password=(os.getenv("PASSWORD")),
    database=(os.getenv("NAME"))
) 

#note
cur = connection.cursor()

cur.execute("""
    SELECT * FROM test_table;""")

cur.fetchall()

print(connection.is_connected())

connection.close()

# Context manager:

# get_db_connection = lambda: connect(
    # FILL IN BLANKS
#     autocommit = True
# ) 

# Template literals work when you put quotes around the literal
# name = 'Joe'

# with get_db_connection() as conn:
#     with conn.cursor() as cur:
#         cur.execute(f"INSERT INTO test_table (name) VALUES ('{name}');")
#         conn.commit()
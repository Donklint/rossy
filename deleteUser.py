import mysql.connector
from db_connect import db_config

which_user = input("Which user do want to delete from the database? : ")
user_upn = input(F"Okay {which_user}? State users UPN: ")

data = (which_user, user_upn)

def delete_user(data):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # SQL query to delete data
        delete_query = "DELETE FROM FussUserTable WHERE fuss_user_firstname = %s AND fuss_user_upn = %S"

        # Insert data into the database
        cursor.execute(delete_query, data)
        conn.commit()

        print("Data deleted successfully.")
    except mysql.connector.Error as err:
        print("Data Not Deleted:", err)

delete_user(data)


import mysql.connector
from db_connect import db_config
from user_rand_keys import generate_id
from user_rand_keys import insert_generate_id

first_name = input('Enter your first name: ')
second_name = input('Enter your second name:')
user_age = input('Age: ')
gender = input('Gender: ')
marital_status = input('Marital status: ')

data = (first_name, second_name, user_age, gender, marital_status)


def populate_database(data):

    try:
        # Establish a connection
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # SQL query to insert data
        insert_query = "INSERT INTO FussUserTable (fuss_user_firstname, fuss_user_age, " \
                       "fuss_user_gender, fuss_user_maritalstts) VALUES (%s, %s, %s, %s)"

        # Insert data into the database
        cursor.execute(insert_query, data)
        conn.commit()

        print("Data inserted successfully.")
    except mysql.connector.Error as err:
        print("Data Not Added:", err)

populate_database(data)

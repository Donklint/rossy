import mysql.connector
from db_connect import db_config

first_name = input('Enter your first name: ')
second_name = input('Enter your second name:')
user_age = input('Age: ')
gender = input('Gender: ')
marital_status = input('Marital status: ')
user_prin_name = input('Enter desired user name: ')
pass_code = input('Set Password: ')

data = (first_name, second_name, user_age, gender, marital_status, user_prin_name, pass_code)


def populate_database(data):

    try:
        # Establish a connection
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # SQL query to insert data
        insert_query = "INSERT INTO FussUserTable (fuss_user_displayname, fuss_user_tenantlvl, fuss_user_firstname, " \
                       "fuss_user_familyname, fuss_user_age, " \
                       "fuss_user_gender, fuss_user_maritalstts, fuss_user_upn, fuss_user_password) " \
                       "VALUES ('BILL.NEIL', 'test', %s, %s, %s, %s, %s, %s, %s)"

        # Insert data into the database
        cursor.execute(insert_query, data)
        conn.commit()

        print("Data inserted successfully.")
    except mysql.connector.Error as err:
        print("Data Not Added:", err)

populate_database(data)

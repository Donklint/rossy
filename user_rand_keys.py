import mysql.connector
import random
import string

# Database connection parameters
db_config = {
    "host": "localhost",
    "user": "mansoft",
    "password": "$F#%=%0Ru}5hB",
    "database": "Fuss"
}

def generate_id(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def insert_generate_id(num_strings):
    try:
        # Establish a connection
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Generate and insert random strings
        for _ in range(num_strings):
            tenantlvl = generate_id(15)
            familyname = generate_id(10)
            displayname = generate_id(5)
            user_prin_name = generate_id(5)
            user_pass = generate_id(8)
            insert_query = "INSERT INTO FussUserTable (fuss_user_tenantlvl, fuss_user_familyname, fuss_user_displayname, fuss_user_upn, fuss_user_password) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(insert_query, (tenantlvl, familyname, displayname, user_prin_name, user_pass))
            conn.commit()

        print("Tenant Level inserted successfully.")

    except mysql.connector.Error as err:
        print("Error:", err)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    num_strings = 10  # Number of random strings to generate and insert
    insert_generate_id(num_strings)

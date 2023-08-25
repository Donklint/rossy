import mysql.connector

# Database connection parameters
db_config = {
    "host": "localhost",
    "user": "mansoft",
    "password": "$F#%=%0Ru}5hB",
    "database": "Fuss"
}

# Sample data to populate the database
sample_data = [
    ("John", "Samson", 25, "John Samson", "tenant01", "Sam@fuss", "SamPass"),
    ("Jane", "Darlene", 30, "Jane Darlene", "tenant01", "Jane@fuss", "JanePass"),
    ("Michael", "Ombuna", 28, "Michael Ombuna", "tenant01", "Mike@fuss", "MikePass")
]

def populate_database(data):
    try:
        # Establish a connection
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # SQL query to insert data
        insert_query = "INSERT INTO FussUserTable (fuss_user_firstname, fuss_user_familyname, fuss_user_age, fuss_user_displayname, fuss_user_tenantlvl, fuss_user_upn, fuss_user_password) VALUES (%s, %s, %s, %s, %s, %s, %s)"

        # Insert data into the database
        cursor.executemany(insert_query, data)
        conn.commit()

        print("Data inserted successfully.")

    except mysql.connector.Error as err:
        print("Data Not Added:", err)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    populate_database(sample_data)

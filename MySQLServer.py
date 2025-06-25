import mysql.connector

# MySQL connection details
# IMPORTANT: Replace 'your_username' and 'your_password' with your actual MySQL credentials
# You might also need to change 'localhost' and '3306' if your MySQL server is elsewhere
DB_CONFIG = {
    'host': 'localhost',
    'user': 'your_username',  # <--- REPLACE WITH YOUR MySQL USERNAME
    'password': 'your_password',  # <--- REPLACE WITH YOUR MySQL PASSWORD
    'port': 3306 # Default MySQL port, change if yours is different
}

DATABASE_NAME = 'alx_book_store'

try:
    # Connect to MySQL server without specifying a database initially
    # This allows us to create a database if it doesn't exist
    cnx = mysql.connector.connect(**DB_CONFIG)
    cursor = cnx.cursor()

    # SQL statement to create the database if it does not exist
    # Using IF NOT EXISTS ensures the script does not fail if the DB already exists
    create_db_query = f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME}"
    cursor.execute(create_db_query)

    print(f"Database '{DATABASE_NAME}' created successfully!")

except mysql.connector.Error as err:
    # Handle connection errors or other database errors
    if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
        print("Error: Access denied. Check your username and password.")
    elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
        print(f"Error: Database '{DATABASE_NAME}' does not exist (this should not happen for CREATE DATABASE, but good to catch).")
    else:
        print(f"Error connecting to MySQL: {err}")
finally:
    # Ensure cursor and connection are closed
    if 'cursor' in locals() and cursor is not None:
        cursor.close()
    if 'cnx' in locals() and cnx.is_connected():
        cnx.close()

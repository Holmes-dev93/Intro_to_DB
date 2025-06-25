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

DATABASE_NAME = 'alx_book_store' # This variable is used for the print statement

# Initialize cnx and cursor to None outside the try block
# This ensures they are defined even if the connection fails, for the finally block
cnx = None
cursor = None

try:
    # Connect to MySQL server without specifying a database initially
    # This allows us to create a database if it doesn't exist
    cnx = mysql.connector.connect(**DB_CONFIG)
    cursor = cnx.cursor()

    # SQL statement to create the database if it does not exist
    # Using IF NOT EXISTS ensures the script does not fail if the DB already exists
    # All SQL keywords are in uppercase as required by general objectives
    create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store" # Changed to a direct string
    cursor.execute(create_db_query)

    print(f"Database '{DATABASE_NAME}' created successfully!")

except mysql.connector.Error as err:
    # Handle specific MySQL errors for better feedback
    if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
        print("Error: Access denied. Check your username and password.")
    elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
        # This case is less likely for CREATE DATABASE but included for completeness
        print(f"Error: The database '{DATABASE_NAME}' could not be found.")
    else:
        print(f"Error connecting to MySQL: {err}")
    # Additional print for general connection failure if cnx is still None
    if cnx is None:
        print("Failed to establish a connection to the MySQL server.")
finally:
    # Ensure cursor and connection are closed properly to free resources
    if cursor: # Checks if cursor object was successfully created
        cursor.close()
    if cnx and cnx.is_connected(): # Checks if connection object exists and is connected
        cnx.close()

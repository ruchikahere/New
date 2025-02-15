import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",       # database server
    user="your_username",   # database username
    password="your_password", # database password
    database="your_database"  # name of your database
)

cursor = conn.cursor()  # Helps in executing SQL queries

import pandas as pd
import mysql.connector
from mysql.connector import Error

# Load CSV file
df = pd.read_csv('student_data.csv')

try:
    # Connect to MySQL
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='rohini',
        database='student_db'
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # Optional: Create table if not exists
        create_table_query = """CREATE TABLE IF NOT EXISTS student_info (
            student_id INT AUTO_INCREMENT PRIMARY KEY,
            sessions_count INT,
            avg_test_score FLOAT,
            dropped_out BOOLEAN
        )
        """
        cursor.execute(create_table_query)
        connection.commit()

        # Insert dataframe rows into MySQL table
        for i, row in df.iterrows():
            sql = "INSERT INTO student_info (sessions_count, avg_test_score, dropped_out) VALUES (%s, %s, %s)"
            values = (int(row['sessions_count']), float(row['avg_test_score']), bool(row['dropped_out']))
            cursor.execute(sql, values)

        connection.commit()
        print(f"{cursor.rowcount} rows inserted successfully.")

except Error as e:
    print(f"Error: {e}")


import pandas as pd
import mysql.connector

class Database:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def create_table(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS EmployeePerformance (
            id INT AUTO_INCREMENT PRIMARY KEY,
            employee_id INT,
            department VARCHAR(255),
            performance_score DECIMAL(5,2),
            years_with_company INT,
            salary DECIMAL(10,2)
        );
        """
        self.cursor.execute(create_table_query)
        self.connection.commit()

    def insert_data(self, query, data):
        self.cursor.executemany(query, data)
        self.connection.commit()

    def fetch_data(self, query):
        self.cursor.execute(query)
        return pd.DataFrame(self.cursor.fetchall(), columns=[desc[0] for desc in self.cursor.description])

import pandas as pd
from database import Database

class CSVImporter:
    def __init__(self, db):
        self.db = db

    def import_csv(self, file_path):
        df = pd.read_csv(file_path)
        insert_query = """
        INSERT INTO EmployeePerformance (employee_id, department, performance_score, years_with_company, salary)
        VALUES (%s, %s, %s, %s, %s)
        """
        data = [tuple(row) for row in df.to_numpy()]
        self.db.insert_data(insert_query, data)
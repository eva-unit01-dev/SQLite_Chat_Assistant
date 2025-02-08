import sqlite3
import re
from datetime import datetime

class QueryHandler:
    def __init__(self, db_path='company.db'):
        self.db_path = db_path

    def execute_query(self, sql_query, params=()):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        try:
            cursor.execute(sql_query, params)
            results = cursor.fetchall()
            column_names = [description[0] for description in cursor.description]
            conn.close()
            return results, column_names
        except sqlite3.Error as e:
            conn.close()
            raise Exception(f"Database error: {str(e)}")

    def parse_query(self, natural_query):
        # Convert query to lowercase for easier matching
        query = natural_query.lower()
        
        try:
            # Pattern matching for different query types
            if "show me all employees in" in query or "list all employees in" in query:
                department = re.search(r'in the (\w+) department', query)
                if department:
                    return self.get_employees_by_department(department.group(1))

            elif "who is the manager of" in query:
                department = re.search(r'manager of the (\w+) department', query)
                if department:
                    return self.get_department_manager(department.group(1))

            elif "list all employees hired after" in query:
                date_match = re.search(r'hired after (\d{4}-\d{2}-\d{2})', query)
                if date_match:
                    return self.get_employees_hired_after(date_match.group(1))

            elif "total salary expense for" in query:
                department = re.search(r'expense for the (\w+) department', query)
                if department:
                    return self.get_department_salary(department.group(1))

            return "I'm sorry, I don't understand that query. Please try rephrasing it."

        except Exception as e:
            return f"Error processing query: {str(e)}"

    def get_employees_by_department(self, department):
        sql = '''
        SELECT Name, Salary, Hire_Date 
        FROM Employees 
        WHERE LOWER(Department) = LOWER(?)
        '''
        results, columns = self.execute_query(sql, (department,))
        if not results:
            return f"No employees found in the {department} department."
        
        return self.format_results(results, columns)

    def get_department_manager(self, department):
        sql = '''
        SELECT Manager 
        FROM Departments 
        WHERE LOWER(Name) = LOWER(?)
        '''
        results, columns = self.execute_query(sql, (department,))
        if not results:
            return f"No manager found for the {department} department."
        
        return f"The manager of the {department} department is {results[0][0]}."

    def get_employees_hired_after(self, date):
        sql = '''
        SELECT Name, Department, Hire_Date 
        FROM Employees 
        WHERE Hire_Date > ?
        '''
        results, columns = self.execute_query(sql, (date,))
        if not results:
            return f"No employees found hired after {date}."
        
        return self.format_results(results, columns)

    def get_department_salary(self, department):
        sql = '''
        SELECT SUM(Salary) as Total 
        FROM Employees 
        WHERE LOWER(Department) = LOWER(?)
        '''
        results, columns = self.execute_query(sql, (department,))
        if not results and results[0][0]:
            return f"No salary data found for the {department} department."
        
        return f"Total salary expense for the {department} department is ${results[0][0]:,}"

    def format_results(self, results, columns):
        if not results:
            return "No results found."
            
        # Format the results as a string
        output = []
        for row in results:
            row_dict = dict(zip(columns, row))
            output.append(" | ".join(f"{col}: {val}" for col, val in row_dict.items()))
        
        return "\n".join(output)
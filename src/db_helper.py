import mysql.connector

class DbHelper:
    def get_maximum_salary(self,cursor):
        '''
        Implement the logic to find and return maximum salary from employee table
        '''
        query = '''select max(emp_salary) from employee_details'''
        cursor.execute(query)
        db = cursor.fetchall()
        for data in db:
            yield data

    def get_minimum_salary(self,cursor):
        '''
        Implement the logic to find and return minimum salary from employee table
        '''
        query = '''select min(emp_salary) from employee_details'''
        cursor.execute(query)
        db = cursor.fetchall()
        for data in db:
            yield data

if __name__ == "__main__":
    db_helper = DbHelper()
    connection = mysql.connector.connect(host="localhost", port="3306", user="root", password="", database="employee")
    cursor = connection.cursor()
    min_salary = db_helper.get_minimum_salary(cursor)
    max_salary = db_helper.get_maximum_salary(cursor)
    for data in min_salary:
        print(data[0])
    for data in max_salary:
        print(data[0])
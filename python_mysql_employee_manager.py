import mysql.connector
from mysql.connector import Error


try:

    con = mysql.connector.connect(
        host = 'host_name',
        user = 'elroberto',
        password = 'TacosR4Life!',
        database = 'Work')
    print("Connection Successful")
except Error as e:
    print(e)

cursor = con.cursor(buffered = True)

def test_database():
    sql = 'Select * From Employee'

    cursor.execute(sql)

    test = cursor.fetchall()

    print(test)



#Format of current Employee Table in Work database: 

# emp_id(int, Primary key), F_name(varchar(50)), L_name(varchar(50)), DOB(date) date_format = 'YYYY-MM-DD'


def Add_Employee():
    employee_id = input("Please enter the Employee's id: ")
    employee_id = int(employee_id)
    f_name = input("First name of the Employee: ").title()
    l_name = input("Last name of the Employee: ").title()
    dob = input("date of birth of the employee(YYYY-MM-DD): ")

    
    sql = "Insert into Employee(emp_id, F_name, L_name, DOB) values(%s,%s,%s,%s)"
    data = (employee_id, f_name, l_name, dob)
    try:
        cursor.execute(sql, data)
    except Error as e:
        print(e)
    con.commit()





def Delete_Employee():
    employee_id = input("Please enter the Employee's id: ")
    employee_id = int(employee_id)
    cursor.execute(f"Select* from Employee Where emp_id = {employee_id}")
    c = cursor.fetchall()
    if c == []:
        print("Please enter a valid employee id ")
        exit()
    else:
        cursor.execute(f"Select f_name from Employee Where emp_id = {employee_id}")
        b = cursor.fetchall()
        a = input(f"Delete {b}? (y/n) ").lower().strip()
        if a =="y":
            cursor.execute(f"Delete from Employee Where emp_id = {employee_id}")

    con.commit()
    

test_database()
print("Menu: 1. Add Employee to database. ")
print("      2. Delete Employee from database. ")
question = input("Press 1. to add any employee. Press 2. to delete an employee. ")

while question.isalpha() != False:
    question = input("Please enter a valid response: ")

question = int(question)

while question <1 or question >3:
    question = input("Please enter a valid response: ")
    question = int(question)

if question == 1:
    try: 
        Add_Employee()
    except Error as h:
        print(h)
    else:
        print("Employee added successfully!")

elif question == 2:
    try:
        Delete_Employee()
    except Error as h:
        print(h)
    else:
        print("Employee deleted successfully!")

elif question == 3:
    print("This feature is still being developed. Please check back later. Thanks and have a great day!")
    exit()




test_database()
cursor.close()


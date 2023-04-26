
class Employees:
    employees_list = {}
    last_employee_id = 0

    def __init__(self):
        self.id = None
        self.role = None
        self.name = None

    def add_employee(self):
        self.name=input("Enter Employee Name:")
        self.role=input("Enter Employee Role:")
        self.id=Employees.last_employee_id +1
        Employees.last_employee_id += 1
        Employees.permanent_employees[Employees.last_employee_id]=self

    def get_employee(self):
        print('Id: ', self.id)
        print('Name: ', self.name)
        print('Role: ', self.role)











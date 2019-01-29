# employee obejct with reference variable
class Employee:
    def __init__(self, eid, ename, eaddr, edesg, esal):
        self.emp_id = eid
        self.emp_name = ename
        self.emp_address = eaddr
        self.emp_designation = edesg
        self.emp_sal = esal

    def display(self):
        print("Employee ID", self.emp_id)
        print("Employee Name", self.emp_name)
        print("Employee Address", self.emp_address)
        print("Employee Designation", self.emp_sal)


m1 = int(input("Enter the Employee ID :"))
m2 = input("Enter the Employee Name :")
m3=input("Enter the Employee Address :")
m4 = input("Enter the Employee Designation :")
m5 = int(input("Enter the Employee Salary :"))
e1 = Employee(m1, m2, m3, m4, m5)
e1.display()
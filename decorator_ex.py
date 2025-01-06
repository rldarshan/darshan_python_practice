
class Employee():
    def __init__(self, emp_name, emp_code):
        self.first_name = emp_name
        self._emp_code = emp_code

    def display(self):
        print("Employee Name: ", self.first_name)
        print("Employee Code: ", self._emp_code)

    @property
    def emp_code(self):
        return self._emp_code

    @emp_code.setter
    def emp_code(self, code):
        self._emp_code = code

emp_1 = Employee('Rama', 101)
emp_1.display()

emp_1.emp_code = 102
emp_1.display()
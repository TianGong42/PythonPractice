class Employee():
    """记录员工的姓氏、名字、工资"""
    def __init__(self, firstname,lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
    def give_raise(self, money=""):
        """给员工加工资，默认5000，也可以有其他数字"""
        if money:
            self.salary = self.salary + money
        else:
            self.salary = self.salary + 5000

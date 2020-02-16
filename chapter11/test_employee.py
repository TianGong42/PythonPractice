import unittest
from employee import Employee
class TestEmployee(unittest.TestCase):
    """针对Employee类的测试"""
    def setUp(self):
        """创建一个Employee对象，供测试使用"""
        self.salary = 138000
        self.defaulraise = 5000
        self.custonraise = 8000
        self.my_employee = Employee("su","ye",self.salary)
    def test_give_default_raise(self):
        """默认加工资数量"""
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.salary, self.salary + self.defaulraise)
    def test_give_custom_raise(self):
        """给定数量的加工资方式"""
        self.my_employee.give_raise(self.custonraise)
        self.assertEqual(self.my_employee.salary, self.salary + self.custonraise)

unittest.main()

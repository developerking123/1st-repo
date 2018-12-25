'''
Write a test case for Employee. Write two test methods, test_give_
default_raise() and test_give_custom_raise(). Use the setUp() method so
you don’t have to create a new employee instance in each test method. Run
your test case, and make sure both tests pass.'''
from Employee_Class import Employee
import unittest
class TestEmployee(unittest.TestCase):
	def setUp(self):
		self.employee1 = Employee("Abdul", "Saboor", 5000)
		
	def test_give_default_raise(self):
		self.employee1.give_raise()
		self.assertEqual(employee1.annual_salary, 10000)
		
	def test_give_custom_raise(self):
		employee1.give_raise(3000)
		self.assertEqual(employee1.annual_salary, 5000+3000)
		
unittest.main()
	


class Employee():
	def __init__(self, first_name, last_name, annual_salary):
		self.first_name = first_name
		self.last_name = last_name
		self.annual_salary = annual_salary
			
	def give_raise(self, new_raise_amount = 5000): #If we want method overloading in python we can use default argument
		self.annual_salary += new_raise_amount
		
	def total_salary(self):
		s = "Total salary of "+self.last_name+" is "+str(self.annual_salary)
		print(s)
		
employee1  = Employee("Abdul", "Saboor", 5000)

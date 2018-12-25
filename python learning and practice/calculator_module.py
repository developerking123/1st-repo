class Calculator():
	def __init__(self, num1, num2):
		self.num1 = num1
		self.num2 = num2
		
	def display_numbers(self):
		print("1st Number: "+str(self.num1))
		print("2nd Number: "+str(self.num2))
		
class Add(Calculator):
	def __init__(self, num1, num2):
		super().__init__(num1, num2)
		
	def add(self):
		return self.num1 + self.num2

class Subtract(Calculator):
	def __init__(self, num1, num2):
		super().__init__(num1, num2)
		
	def sub(self):
		return self.num1 - self.num2

class Product(Calculator):
	def __init__(self, num1, num2):
		super().__init__(num1, num2)
		
	def mul(self):
		return self.num1 * self.num2

class Divide(Calculator):
	def __init__(self, num1, num2):
		super().__init__(num1, num2)
		
	def div(self):
		return self.num1 / self.num2
		
			
			

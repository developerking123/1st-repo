'''We have made calculator_module in which we store 5 classes
1- Calculator   2- Add   3- Subtract 4- Product  5- Divide
Now we import the module and use classesd differently'''
# 1st Method: Import single class from module
from calculator_module import Calculator 
cal = Calculator(2, 4)
print(cal.num1)
print(cal.num2)
print(cal.display_numbers())

# 2nd Method: Import many classes from module
from calculator_module import Calculator, Add, Subtract, Product, Divide 
cal1 = Calculator(5,10)
print(cal1.num1)
print(cal1.num2)
print(cal1.display_numbers())

add1 = Add(5, 10)
print(add1.add())

sub1 = Subtract(5, 10)
print(sub1.sub())

mul1 = Product(5, 10)
print(mul1.mul())

div1 = Divide(5, 10)
print(div1.div())


# 3rd Method: Importing an entire module
import calculator_module
cal1 = calculator_module.Calculator(10,20)
print(cal1.num1)
print(cal1.num2)
print(cal1.display_numbers())

add1 = calculator_module.Add(10, 20)
print(add1.add())

sub1 = calculator_module.Subtract(10, 20)
print(sub1.sub())

mul1 = calculator_module.Product(10, 20)
print(mul1.mul())

div1 = calculator_module.Divide(10, 20)
print(div1.div())

# 4th Method: Importing all classes from module
from calculator_module import*

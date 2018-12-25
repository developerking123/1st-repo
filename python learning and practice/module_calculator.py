'''sab se bara faida module banane ka k ye logic chupa deta h'''
import calculator # imported module (1st method)(ppora module uthakar le aaya)
print(calculator.add(2,4)) # caculator is a module and add is function in module
print(calculator.sub(2,4))
print(calculator.mul(2,4))
print(calculator.div(4,2))

from calculator import add # 2nd method calculator k module se sirf add ka function utha kar laya
print(add(5, 5))
print(add(5, 14))

from calculator import add, sub # 1 se ziada jitne func chahain import kara sakte hain
print(add(5, 10))
print(sub(14, 10))

import calculator as cal # 3rd method(Aliasing) Giving short name to imported module 
print(cal.add(2,4)) 
print(cal.sub(2,4))
print(cal.mul(2,4))
print(cal.div(4,2))

from calculator import mul as m, div as d # aliasing on function 
print(m(5, 10))
print(d(14, 28))

from calculator import* #4th method(importing all functions exist in module)



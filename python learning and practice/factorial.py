def FirstFactorial(num): 
	# code goes here
	factorial = 1
	for i in range(num,0,-1):
		factorial *= i
	return factorial
    
# keep this function call here  
num = int(input("Enter the number whoose factorial you want: "))
fact = FirstFactorial(num)
print(fact)
















  

word = input("Enter an string: ") 
print(len(word))
str1 = ''
for i in range(len(word)-1,-1,-1):
	print(i)
	str1+= word[i]
print(str1)



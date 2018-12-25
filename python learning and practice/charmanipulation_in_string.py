str = input("Enter an :string: ")
str1 = ''
for i in str:
	if (ord(i) >= ord('a')) and (ord(i) <= ord('y')):
		if(chr(ord(i)+1) == 'a') or (chr(ord(i)+1) == 'e')or (chr(ord(i)+1) == 'i')or (chr(ord(i)+1) == 'o')or(chr(ord(i)+1) == 'u'):
			i = chr(ord(i)-32)
		str1+= chr(ord(i)+1)
	else:
		str1 += i
		
				
print (str1)


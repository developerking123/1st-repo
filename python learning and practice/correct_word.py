word = input("Enter a character sequence: ")
result = 0
for i in range(1,len(word)-1):
	if (word[0] >= 'a') and (word[0] <= 'z'):
		result+=1
		break
	elif (word[i] >= 'a') and (word[i] <= 'z'):
		print('in elif :'+str(i))
		if((word[i-1] != '+') and (word[i+1] != '+')):
			print('in elif: if')
			result += 1
			break
if result > 0:
	print("true")
else:
	print("false")

prime_range = int(input("Enter the range of prime no: "))
prime_list = [2]
for i in range(3, prime_range,2):
	prime = True
	for j in range(3, int(i/2),2):
		print(str(i)+" % " + str(j))
		if i % j == 0:
			prime = False
			break
	if prime:
		prime_list.append(i)
print(prime_list)


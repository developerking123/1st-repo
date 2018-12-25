sentence = input("Enter a sentence: ")
words = sentence.split()
m = 0
word_length = []
for word in words:
	n = 0
	for letter in word:
		if letter.isalpha():
			n+= 1
	word_length.append(n)
largest = max(word_length)
for i in word_length:
	if i == largest:
		break
	m+= 1
print(words[m])
	
	

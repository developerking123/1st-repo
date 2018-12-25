def Words(sentence):
	no_of_words = sentence.split()
	init = 0;
			
	return no_of_words
	
def Chars(no_of_words):
	length_of_word = []
	for i in range(0,len(no_of_words)):
		length_of_word.append(len(no_of_words[i]))
		
	return length_of_word
	
def Largest_word(no_of_words,no_of_chars_in_word):
	index_of_largest_word = 0
	largest_word = no_of_chars_in_word[0]
	for i in range(0,len(no_of_words)):
		if(largest_word < no_of_chars_in_word[i]):
			largest_word = no_of_chars_in_word[i]
			index_of_largest_word = i
			
	print('The largest word is '+no_of_words[index_of_largest_word]+ 
	" whose character are "+str(largest_word))  
		
sentence = input("Enter an string: ")
no_of_words = Words(sentence)
print(no_of_words)
no_of_chars_in_word = Chars(no_of_words)
print(no_of_chars_in_word)
Largest_word(no_of_words,no_of_chars_in_word)

#class GenerateMarksheet():
#	def(self,)
student_name=input('Enter Student Name: ')
registeration_no=input('Enter Student Registration Number: ')
examination_year=int(input('Enter Student Examination Year: '))
roll_no=input('Enter Student Roll Number: ')
exam_type=input('Enter Exam Type: ')


no_of_courses=int(input('Enter Number Of Courses You Are Taken: '))
courses=[]
for i in range(1,no_of_courses+1):
	course=input('Enter the name of Course '+str(i)+': ')
	courses.append(course)
print('\n\n')
	
gained_numbers=[]
total_no_of_courses=[]
sum_of_total_numbers=0

for course in courses:
	total_no_of_course=int(input('Enter the total no.s of '
	                              +course+':  '))
	sum_of_total_numbers+=total_no_of_course
	total_no_of_courses.append(total_no_of_course)

print('\n')
i=0 #variable taken for iterating index of total_no_of_subjects(list variable)

sum_of_gained_numbers=0
for course in courses:
	gained_no=int(input('Enter the number gained in '+course+
	                    ' out of '+str(total_no_of_courses[i])+' : '))
	sum_of_gained_numbers+=gained_no
	gained_numbers.append(gained_no)
	i+=1
	
s=''
n=0 #variable taken for iterating no.s list index
for course in courses:
	s+=''+course+'\t:\t'+str(gained_numbers[n])+'/'+str(total_no_of_courses[n])+'\n'
	n+=1
	percentage=(sum_of_gained_numbers/sum_of_total_numbers)*100
print('Name\t:\t'+student_name)
print('Registration Number\t:\t'+registeration_no)
print('Roll No\t:\t'+roll_no)
print('Examination Year\t:\t'+str(examination_year))	
print('Exam Type\t:\t'+exam_type)
print(s)
	
print('Percentage\t:\t%.2f'%percentage+' %') #for limiting the digits after decimal upto 2

if percentage >= 90:
	grade='A+'
	
elif percentage >= 79.5 and percentage <=89.5:
	grade='A'
	
elif percentage >= 69.5 and percentage <=79.4:
	grade='B' 

elif percentage >= 59.5 and percentage <=69.4:
	grade='C' 

elif percentage >= 49.5 and percentage <=59.4:
	grade='D' 

elif percentage >= 39.5 and percentage <=49.4:
	grade='E' 

elif percentage < 39.5:
	grade='F' 
	
print('Grade\t:\t'+grade)


if grade == 'A+':
	remarks='Best'
	
elif grade =='A':
	remarks='Excellent'		 

elif grade =='B':
	remarks='Good'		 

elif grade =='C':
	remarks='Need Improvement'		 

elif grade =='D':
	remarks='Not Good'		 

elif grade =='E':
	remarks='Poor'		 

elif grade =='F':
	remarks='Fail'		 

print('Remarks\t:\t'+remarks)

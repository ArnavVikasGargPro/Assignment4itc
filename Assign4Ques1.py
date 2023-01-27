'''ques 1 --A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.'''
m=int(input("Please enter your marks ="))
if(m<=100 and m>80):
		print("YOUR TOTAL MARKS IS ",m," GRADE-A");
	
elif(m<=80 and m>60) :
		print("YOUR TOTAL MARKS IS ",m," GRADE-B");
	
elif(m<=60 and m>50) :
		print("YOUR TOTAL MARKS IS ",m," GRADE-C");
	
elif(m<=50 and m>45) :
		print("YOUR TOTAL MARKS IS ",m," GRADE-D");
	
elif(m<=45 and m>25) :
		print("YOUR TOTAL MARKS IS ",m," GRADE-E");
	
	
elif(m<=25 and m>0):
		print("YOUR TOTAL MARKS IS ",m," GRADE-Fail");
	

else:
		print(" your input marks is out of range ");

#ece 22105015
		
	


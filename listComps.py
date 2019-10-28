# -*- coding: utf-8 -*-
# @Author: sabrina
# @Date:   2019-09-11 19:38:13
# @Last Modified by:   sabrina
# @Last Modified time: 2019-10-14 22:45:12


if __name__ == '__main__':
	A = [1,2,3,4,5]
	B = [2,4,6,8,10]

	I = [-1, 0, 1, 2]
	R = [2.7818, -3.14159]

	# Task #1 -- multiplies all of the elements of A by 7.

	# traverse through A
	# multiplying each element passed
	S = [i * 7 for i in A]
	print("Task #1: ", S)


	# Task #2 -- adds all of the elements of A with all of the elements of B

	# traverse through A and B
	# if index of A and B are the same, append to Plus
	Plus = [A[i] + B[j] for i in range(len(A)) for j in range(len(B)) if i == j]
	print("Task #2: ", Plus)


	# Task #3 -- takes all of the elements of A and selects only those elements of A that are even.

	# traverse through A
	# even logic (i % 2 == 0) appends i if true
	Even = [i for i in A if i % 2 == 0]
	print("Task #3: ", Even)


	# Task # 4 -- uses the elements of both I and R, and selects only those elements of both I and R that are non-negative, integer numbers.

	# combine lists I and R into one
	# the function `isinstance()` checks if x is an integer
	# check if x is greater than or equal to 0
	NonNeg = [x for x in I + R if isinstance(x, int) and x >= 0]

	# # change x in R and I to int
	# # check if x greater or equal to 0
	# NonNeg = [int(x) for x in I + R if x >= 0]

	print("Task #4: ", NonNeg)

	# are we changing values in R to int or checking if they are int?

# END OF PROGRAM
'''
NOTES: 

The basic syntax is
	[ expression for item in list if conditional ]
This is equivalent to:
	for item in list:
	    if conditional:
	        expression


If you used to do it like this:
	new_list = []
	for i in old_list:
	    if filter(i):
	        new_list.append(expressions(i))
You can obtain the same thing using list comprehension:
	new_list = [expression(i) for i in old_list if filter(i)]



CS131B LAB 10
Purpose:  Use list comprehensions to create lists that match certain criteria.

Lab

For the following lists:

	A = [1,2,3,4,5]
	B = [2,4,6,8,10]

	I = [-1, 0, 1, 2]
	R = [2.7818, -3.14159]

Write a Python program that uses the lists, and performs the following tasks:

Task #1 -- Make a list comprehension that makes a list which multiplies all of the elements of A by 7.  Store this list in a variable called S.  Once S is made, print S.

Task #2 -- Make a list comprehension that adds all of the elements of A with all of the elements of B.  Store this list in a variable called Plus.  Once Plus is made, print Plus.  Note:  For this you should use two for loops.

Task #3 -- Make a list comprehension that takes all of the elements of A and selects only those elements of A that are even.  Store this list in a variable called Even.  Once Even is made, print Even.  

Note:  There is a test that can return a true/false value which states if a number is even:  

    if a number % 2 (that is, number modulus 2) is equal to 0, then the number is even.  Otherwise it will be equal to 1, and that means the number is odd.

Task # 4 --  Make a list comprehension that uses the elements of both I and R, and selects only those elements of both I and R that are non-negative, integer numbers.  Store this list in a variable called NonNeg.  Once NonNeg is made, print NonNeg.  Notes:

	a)  For this you should use two for loops.
	b)  A non-negative integer is a number that is greater than or equal to zero, and is a whole number (that is, it has no values after the decimal point, or it only has numbers with the value 0 after the decimal point.  Integers can be made by using the int(x) function, which will take any numeric value for x and turn it into an integer.


Make sure you use comments for each of the tasks explaining what your programming logic is for each list comprehension. 

Name the program source code file listComps.py and submit the required file here in Canvas. This assignment is worth 80-points, to be awarded after all labs are successfully completed. Submit your assignment as listComps.py making sure you put the ".py" file extension at the end of the file name. Submit listComps.py using the "Submit Assignment" button, and use the "File Upload" tab to select listComps.py from your computer to send it to the instructor.
'''
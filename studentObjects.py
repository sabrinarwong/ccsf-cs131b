# -*- coding: utf-8 -*-
# @Author: sabrina
# @Date:   2019-09-11 19:36:07
# @Last Modified by:   sabrina
# @Last Modified time: 2019-10-27 22:44:37

# 1. Create an object specification with these seven data fields: name, address, city, state, zip, student id, and gpa. 

# 2. In main, declare 3 uninitialized student objects, using either by making a list of 3 objects or 3 individual objects -- your choice. 

# 3. Write a value-returning function to create and return a single student object. Design console prompts and input statements in the function for the eight data fields. Call the function three times – once to initialize each of main’s student objects. 

# 4. Write a void function to output nicely formatted labels and values for a single student object’s data fields. Call the function three times – once for each student object.


# END OF PROGRAM
'''
CS131B LAB 8
Purpose

Learn how to put an object specification into a program, and how to customize its data fields.
Learn how to declare objects using an object specification, and assign values to its data fields. 
Learn how to use an object as an input parameter in a function call, and as an output value.
Lab
Write a program that the college Admissions office can use to manage the records of students.


Requirements   

Write studentObjects.py, per this specification: 

1. Create an object specification with these seven data fields: name, address, city, state, zip, student id, and gpa. 

2. In main, declare 3 uninitialized student objects, using either by making a list of 3 objects or 3 individual objects -- your choice. 

3. Write a value-returning function to create and return a single student object. Design console prompts and input statements in the function for the eight data fields. Call the function three times – once to initialize each of main’s student objects. 

4. Write a void function to output nicely formatted labels and values for a single student object’s data fields. Call the function three times – once for each student object.
 
Program I/O.
Input: from the console keyboard, the personal information for each of 3 students, one student at a time.
Output: a labeled summary of the personal information as entered for each of 3  students.
 
 
Example. Your program's console I/O should look something like this, where the user input in this example is shown with italics lettering:

	Enter for Student 1  name: Joe Student
	address: 123 Long Road
	city: Happytown
	state: CA
	zip: 98765
	gpa: 2.64
	...8
	Enter for Student 2 name: Ato Kohai
	address: 456 Big Street
	city: Gladville
	...
	Enter for Student 3 name: Nandi Zulu
	address: 789 Grand Street
	city: Joytown
	...
	 Output for Student 1
	name: Joe Student
	address: 123 Long Road
	city: Happytown
	state: CA
	zip: 98765
	gpa: 2.64
	...
	Output for Student 2
	name: Ato Kohai
	address: 456 Big Street
	city: Gladville
	...
	Output for Student 3
	name: Nandi Zulu
	address: 789 Grand Street
	city: Joytown
	...
 
'''
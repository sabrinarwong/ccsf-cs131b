# -*- coding: utf-8 -*-
# @Author: sabrina
# @Date:   2019-09-11 19:36:07
# @Last Modified by:   Sabrina Wong
# @Last Modified time: 2019-10-28 23:09:11


class Student:

	#variables to store student information
	name = None
	address = None
	city = None
	state = None
	zip_code = None
	student_id = None
	gpa = None

	# initialization constructor used when a new instance of the student is created.
	# self is referencing the current object 
	# constructor prompts user input to fill in variables. 
	def __init__(self):
		self.name = input("Enter your name: ")
		self.address = input("Enter your address: ")
		self.city = input("Enter your city: ")
		self.state = input("Enter your state: ")
		self.zip_code = int(input("Enter your zipcode: "))
		self.student_id = int(input("Enter your sid: "))
		self.gpa = float(input("Enter your gpa: "))

		print("\n")

	# self in the parameter is used as a reference to the object data fields. F-strings are used in the print statement for string format syntax with variables. 
	def print(self):
		print(f"name: {self.name}", 
			  f"address: {self.address}", 
			  f"city: {self.city}", 
			  f"state: {self.state}", 
			  f"zip code: {self.zip_code}", 
			  f"student id: {self.student_id}", 
			  f"gpa: {self.gpa}", sep="\n", end="\n\n")

# 2. In main, declare 3 uninitialized student objects, using either by making a list of 3 objects or 3 individual objects -- your choice.
if __name__ == '__main__':
	#array with student objects. Each student object is initialized through the constructor method. 
	students_list = [Student(), Student(), Student()]

	# Loop to print out student object variables. Print() is a method created in the student class. 
	for i in range(len(students_list)):
		print("Output for Student", i+1)
		students_list[i].print()


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
Output: a labeled summary of the personal information as entered for each of 3 students.
 
 
Example. Your program's console I/O should look something like this, where the user input in this example is shown with italics lettering:

	Enter for Student 1 name: Joe Student
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

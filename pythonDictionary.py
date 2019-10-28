# -*- coding: utf-8 -*-
# @Author: Sabrina
# @Date:   2019-09-03 23:12:42
# @Last Modified by:   sabrina
# @Last Modified time: 2019-09-29 19:45:37


# dictionary with all inital values to empty strings
student = {'first name':'', 'last name':'', 'student_id':''}

# user input values for init set of keys
student['first name'] = input("Enter first name: ")
student['last name'] = input("Enter last name: ")
student['student_id'] = input("Enter student_id: ")

# print what init keys and values after user input
print("first name: ", student['first name'])
print("last name: ", student['last name'])
print("student_id: ", student['student_id'])

# begin prompt for loop to add mroe items into `student` dictionary
request = input("Add more to the dictionary? (Y or y for yes) ")
while request == 'y' or request == 'Y':
	# user input for new key and value to student
	newAttribute = input("Enter a kind of information to add: ")
	student[newAttribute] = input("Enter the value for the information to add: ")

	# print all items students
	# .items() method returns (key, value) tuple pairs
	# for k, v in student.items():
	# 	print(k, ": ", v)

	# to repeat or not to repeat
	request = input("Add more to the dictionary? (Y or y for yes) ")

# print out everything one last time.
for k, v in student.items():
	print(k, ": ", v)

# END OF PROGRAM
'''
CS 131B LAB 3
Using a Python Dictionary
Purpose:   Write a program that uses a dictionary that has existing entries, and updates the entries by giving values for any existing keys, as well as allowing the user to add new entries for the dictionary.


The program should be written to have a dictionary that has a group of keys related to basic information about what is often kept in a student information system.  Here is the dictionary:

	student = {'first name':'', 'last name':'', 'student_id':''}

Note:  the
	
	''

value after each key indicates that the value is an empty string.  That value is used to set the initial value of all the dictionary keys to the empty string.

Write this dictionary into your program.

The program should take the user’s input and store the value with its corresponding key.  For example, the program should go through each key in the student dictionary and use the key to give a prompt for the user.

	Enter first name:   
	Enter last name:
	Enter student_id:

For each of these, the user should be allowed to input a value.  Each value should then be stored in the dictionary with its corresponding key.  The value the user gives for first name should be stored with the key 'first name', the value the user gives for last name should be stored with the key 'last name', etc.

Once the values are stored, the program should print out the dictionary keys and values. When printing the keys and values should be displayed this way:

	first name:  value user gave for the first name 
	last name:  value user gave for the last name 
	student_id:  value user gave for the student id
 
After printing the keys and the values the program should ask the user if they wish to store more information in the dictionary.  Here's how the program should prompt the user:

	add more to the dictionary (Y or y for yes):

The user should give a character answer of Y or y if they wish to store information in the dictionary.  Any other input given that is not Y or y is considered to mean that the user does not wish to store more information in the dictionary.  

If the user wants to store more information in the dictionary, the program should prompt the user this way:

	enter a kind of information to add:

The user should then be allowed to give input that will be stored as a new key in the dictionary. The program should then prompt the user this way:

	enter the value for the information to add:

The user should then be allowed to give input that will be stored as a new value in the dictionary.  That new value should be stored as the value associated with the new key the user entered in the "enter a kind of information to add:" prompt.

After the new key and new value are placed into the dictionary, print out all of the dictionary keys and values.  Make sure to print out the dictionary so that each key is printed next to its corresponding value.

Once all of the above logic is working correctly, place all of this logic inside a loop.  The loop should be written to keep asking the user if they want to continue to store more information in the dictionary.  The loop should continue to run if the user wants to store more information in the dictionary.   In other words, if the user give an input of Y or y at this prompt:

	add more to the dictionary (Y or y for yes):

the loop should continue running asking the user if they want to continue to store more information in the dictionary. If the user does not give an input of Y or y at the prompt, the loop should stop.

After the loop stops running, print out the print out all of the dictionary keys and values again.  Once this print out is finished, the program is done and the program should end.
'''
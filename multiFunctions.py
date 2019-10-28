# -*- coding: utf-8 -*-
# @Author: sabrina
# @Date:   2019-09-09 11:08:42
# @Last Modified by:   sabrina
# @Last Modified time: 2019-09-20 14:16:15

import random

# Task 1
def calculate(num1, num2, num3, num4, num5):
	"finds the average of all the values of parameters"

	return (num1 + num2 + num3 + num4 + num5) / 5


# Task 2: from lab 4
def slicings(string, list, tuple):
	"slicing from lab 4"
	# Task #1
	print(string[7:11] + 'e', end = '\n')

	# Task #2
	# because indexing only one element in a list will return the value of that element, it needs to be created into a list to be concatenated with other lists.
	song = [list[6]]
	song.extend(list[-3:])

	# splicing in a tuple starting at index 4 (inclusively) to end at index 6 (exclusively)
	notOff = tuple[4:6]

	# Task #3
	# take user input and use that as the ending index for splicing
	# variables a, b, and c print out the set of characters ranging from index 0 up to the index of the user input value
	numChars = int(input("how many characters you would like to extract? "))
	a = string[:numChars]
	b = list[:numChars]
	c = tuple[:numChars]

	# the argument `sep` separates each printed variable by a newline, 
	# `end` ends the entire print statement by two new lines to separate between tasks
	print(a, b, c, sep = '\n', end = '\n')

	# Task #4
	# negative index number refers to the end of the string as index -1
	# accessing characters starting from index -3 to the end of string results in the last three characters
	a = string[-3:]
	b = list[-3:]
	c = tuple[-3:]

	print(a, b, c, sep = '\n', end = '\n')

	# Task #5
	# the last parameter of string, list, and tuple accessing is a stride, which refers to how many characters to move forward after the first character is retrieved from the string
	# in this case, -1 moves the stride backwards, so the results would take the string, list, and tuple from the end and traverse to the front
	a = string[::-1]
	b = list[::-1]
	c = tuple[::-1]

	print(a, b, c, sep = '\n', end = '\n')

	# Task #6
	# stride by 2 skips every other character 
	a = string[::2]
	b = list[::2]
	c = tuple[::2]

	print(a, b, c, sep = '\n', end = '\n\n')

	pass

def randomChoice(list):
	"returns a random element from given list"
	return random.choice(list)


if __name__ == '__main__':
	# function
	print("Task 1:", calculate(1,2,3,4,5), sep ='\n', end = '\n\n')

	print("Task 2:")
	str = 'Python Slicing'
	l = ['P', 'y', 't', 'h', 'o', 'n', 'S', 'l', 'i', 'c', 'i', 'n', 'g']
	t = ('P', 'y', 't', 'h', 'o', 'n', 'S', 'l', 'i', 'c', 'i', 'n', 'g')
	# function
	slicings(str,l,t)

	colors = ["red", "blue", "green", "yellow", "pink", "black", "white"]
	#function
	print("Task 3:", randomChoice(colors), sep ='\n', end = '\n')

# END OF PROGRAM
'''
CS131B LAB 5
Purpose   Practice using functions -- take calculating and logical tasks, and express them as sub programs.

Lab

Write a function for each of the following tasks:

Task # 1 --write a function that calculates the average value of 5 parameters given to it.  The function should take 5 parameters (assume that the parameters will always be numbers), add all of the values of the parameters together, and then divide the addition by 5.  

	Make sure the function uses the return command to return the average as the value for the function.


Task #2 -- take all the logic from Lab 4, which produces slices, and rewrite the logic in a function called slicings().  slicings should take 3 parameters for the values needed for the slicing logic of Lab 4.  Those 3 parameters should be used to get the string, the list and the tuple given in the Lab 4 description.  Those 3 parameters can have any names you choose to provide, but they must be able to take a string, a list, and a tuple as values passed in by a main program.

	(see Lab 4's description here)

Task # 3 -- write a function that takes as many parameters as you liked (even 0 parameters is appropriate) and either performs a tasks that you choose or returns a value that you choose.

 
For all three tasks, include them in a single Python file.  Also, make a main program in the Python file that gives values to all three tasks.  The main program should call all three functions.

'''
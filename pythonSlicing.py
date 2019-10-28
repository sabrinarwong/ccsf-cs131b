# -*- coding: utf-8 -*-
# @Author: sabrina
# @Date:   2019-09-09 11:07:17
# @Last Modified by:   sabrina
# @Last Modified time: 2019-09-11 19:33:06


def slicingSubmit():
	# init lab variables
	str = 'Python Slicing'
	l = ['P', 'y', 't', 'h', 'o', 'n', 'S', 'l', 'i', 'c', 'i', 'n', 'g']
	t = ('P', 'y', 't', 'h', 'o', 'n', 'S', 'l', 'i', 'c', 'i', 'n', 'g')

	# Task #1
	# slicing takes a range of characters in a string and creates a substring
	newStr = str[7:11] + 'e'
	print(newStr, end = '\n\n')

	# Task #2
	# because indexing only one element in a list will return the value of that element, it needs to be created into a list to be concatenated with other lists.
	song = [l[6]]
	song.extend(l[-3:])

	# splicing in a tuple starting at index 4 (inclusively) to end at index 6 (exclusively)
	notOff = t[4:6]

	# Task #3
	# take user input and use that as the ending index for splicing
	# variables a, b, and c print out the set of characters ranging from index 0 up to the index of the user input value
	numChars = int(input("how many characters you would like to extract? "))
	a = str[:numChars]
	b = l[:numChars]
	c = (t[:numChars])

	# the argument `sep` separates each printed variable by a newline, 
	# `end` ends the entire print statement by two new lines to separate between tasks
	print(a, b, c, sep = '\n', end = '\n\n')

	# Task #4
	# negative index number refers to the end of the string as index -1
	# accessing characters starting from index -3 to the end of string results in the last three characters
	a = str[-3:]
	b = l[-3:]
	c = t[-3:]

	print(a, b, c, sep = '\n', end = '\n\n')

	# Task #5
	# the last parameter of string, list, and tuple accessing is a stride, which refers to how many characters to move forward after the first character is retrieved from the string
	# in this case, -1 moves the stride backwards, so the results would take the string, list, and tuple from the end and traverse to the front
	a = str[::-1]
	b = l[::-1]
	c = t[::-1]

	print(a, b, c, sep = '\n', end = '\n\n')

	# Task #6
	# stride by 2 skips every other character 
	a = str[::2]
	b = l[::2]
	c = t[::2]

	print(a, b, c, sep = '\n', end = '\n\n')

	# in each task (from 3 to 6), the way to access and splice strings, lists, and tuples are the same.

	#END OF PROGRAM

def slicingPretty():
	# init lab variables
	str = 'Python Slicing'
	l = ['P', 'y', 't', 'h', 'o', 'n', 'S', 'l', 'i', 'c', 'i', 'n', 'g']
	t = ('P', 'y', 't', 'h', 'o', 'n', 'S', 'l', 'i', 'c', 'i', 'n', 'g')

	# Task #1
	# slicing takes a range of characters in a string and creates a substring
	newStr = str[7:11] + 'e'

	# print to distinguish output with task number
	print("Task #1", newStr, sep = '\n\t')

	# Task #2
	# because indexing only one element in a list will return the value of that element, it needs to be created into a list to be concatenated with other lists.
	song = [l[6]]
	song.extend(l[-3:])

	# splicing in a tuple starting at index 4 (inclusively) to end at index 6 (exclusively)
	notOff = t[4:6]

	# to show output of Task 2
	print("Task #2", song, notOff, sep = '\n\t')

	# Task #3
	# take user input and use that as the ending index for splicing
	# variables a, b, and c print out the set of characters ranging from index 0 up to the index of the user input value
	numChars = int(input("\nhow many characters you would like to extract? "))
	a = str[:numChars]
	b = l[:numChars]
	c = (t[:numChars])

	# the argument `sep` separates each printed variable by a newline, 
	# `end` ends the entire print statement by two new lines to separate between tasks
	print("Task #3", a, b, c, sep = '\n\t')

	# Task #4
	# negative index number refers to the end of the string as index -1
	# accessing characters starting from index -3 to the end of string results in the last three characters
	a = str[-3:]
	b = l[-3:]
	c = t[-3:]

	print("Task #4", a, b, c, sep = '\n\t')

	# Task #5
	# the last parameter of string, list, and tuple accessing is a stride, which refers to how many characters to move forward after the first character is retrieved from the string
	# in this case, -1 moves the stride backwards, so the results would take the string, list, and tuple from the end and traverse to the front
	a = str[::-1]
	b = l[::-1]
	c = t[::-1]

	print("Task #5", a, b, c, sep = '\n\t')

	# Task #6
	# stride by 2 skips every other character 
	a = str[::2]
	b = l[::2]
	c = t[::2]

	print("Task #6", a, b, c, sep = '\n\t')

def whichSlicing(option):
	switcher = {
		1: slicingSubmit,
		2: slicingPretty,
	}
	return switcher.get(option, lambda: print("invalid option"))

option = int(input("1 for spaced, 2 for pretty: "))
whichSlicing(option)()


# in each task (from 3 to 6), the way to access and splice strings, lists, and tuples are the same.

#END OF PROGRAM
'''
NOTES:
	indexing is accessing and isolating one of the characters in a string
	slicing is taking a range of characters from the string, creating a substring
	stride from slicing (third parameter) refers to how many characters to move forward after the first character is retrieved from the string. (default is 1)
		i.e ss[1:10:2] - `2` skips every other chracter
######
CS 131B - LAB 4
Purpose

In this lab you will practice using slicing on a Python string, a Python list, and a Python tuple.

Lab

Use the following string, list, and tuple:

str = ‘Python Slicing’
l = [‘P’, ‘y’, ’t’, ‘h’, ‘o’, ’n’, ’S’, ‘l’, ‘i’, ‘c’, ‘i’, ’n’, ‘g’]
t = (‘P’, ‘y’, ’t’, ‘h’, ‘o’, ’n’, ’S’, ‘l’, ‘i’, ‘c’, ‘i’, ’n’, ‘g’)

as a part of performing the programming tasks listed below:

Task #1
Print the string ‘Slice’ by taking the str string, extracting ’Slic’ from str using slicing, and printing the ‘Slic’ extracted, and the character ‘e’ after it.

Task #2
Use slicing to get the list [’S’,’i’,’n’,g’] from the list l and store the list [’S’,’i’,’n’,g’] in a variable named song.
Use slicing to get the tuple (‘o’,’n’) from the tuple t and store the tuple (‘o’,’n’) in a variable named notOff.

Task #3
Using the input() command, have a user input how many characters they would like to extract. The input the user gives should be an integer, and should be converted using the int() command. After the input has been converted using int(), use the integer to print the following slices:
a) print a slice starting at the beginning of the str string that has a length equal to the integer from the input
b) print a slice starting at the beginning of the l list that has a length equal to the integer from the input
c) print a slice starting at the beginning of the t tuple that has a length equal to the integer from the input

Task #4
Use negative numbers in slicing to print out the following:
a) the last 3 characters of the string str
b) the last 3 characters of the list l
c) the last 3 characters of the tuple t

Task #5
Use negative numbers and a step value with slicing to print the string str, the list l, and the tuple t backwards.

Task #6
Use a step value with slicing to print every other character from the string str, the list l, and the tuple t starting at the first character.
'''
# -*- coding: utf-8 -*-
# @Author: sabrina
# @Date:   2019-09-11 19:33:40
# @Last Modified by:   sabrina
# @Last Modified time: 2019-10-14 22:42:54

from functools import reduce

if __name__ == '__main__':
	myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

	# Task 1
	# reduce() returns the new reduced result - performs a repetitive operation over the pairs of the list
	maxMyList = reduce(lambda x,y: x if x > y else y, myList)
	print(maxMyList)

	# Task 2
	# map() returns a new list that contains all almbda modified items returned by that function for each item
	# list() returns an actual list of the map
	return_results = list(map(lambda x: x * x, myList))
	print(return_results)
	

# END OF PROGRAM
'''
CS131B LAB 6
In this lab you will write an anonymous functions as well as use map() and list().  You will use anonymous functions to return certain results, and the functions map() and list() to help make a list items from an anonymous function's results.

First, make a list of values from 1 to 10 in your program that looks similar to this:

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
Second, perform the following tasks:

Task # 1 -- write an anonymous function that finds the maximum value of two parameters passed to the function.  Note that you will need to use if: ... else:... logic to find the maximum value of the two parameters.  Using the anonymous function you made to find the maximum value in myList.  Assign the maximum value to the variable maxMyList, and print maxMyList out after it has been assigned.

Task # 2 -- write an anonymous function that takes a single parameter and returns that parameter squared.  In other words, the lambda function returns the single parameter multiplied by itself.  You must use map() to call the lambda function on myList, and return values that the lambda function has used with map() to make the square of each element in myList.  Once you place your lambda function in map(), store the list map() makes into a list variable named return_results.  This means return_results is supposed to be a list of the results of the myList values multiplied by themselves.  Remember, map() returns list items without actually making a list (the technical name for all these items is an iterable).   So you will have to use what map() returns and additional programming logic to make return_results into a list.


Note:  Don't be surprised if this program is short and does not have a lot of Python commands!   That's part of the point of this lab -- to show you that with a simple lambda function used with map() a lot can be done to make a list of useful information.

 '''
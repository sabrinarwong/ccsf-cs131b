# -*- coding: utf-8 -*-
# @Author: Sabrina
# @Date:   2019-08-28 08:47:38
# @Last Modified by:   sabrina
# @Last Modified time: 2019-09-04 13:49:36


import random
# module for randomization functions

numberOfTosses = int(input("Enter the number of tosses to perform: "))
print()
# take user input and convert to an int
# print new line
counter = 0

while counter < numberOfTosses:
# start loop if counter is less than user input

	# if counter == numberOfTosses:
	# 	break
	# # base case, if counter is same as number of tosses, exit loop

	flip = random.randint(0,1)
	# init random variable
	if flip == 0:
		print("Heads")
		# if random function picks 0, print heads
	elif flip == 1:
		print("Tails")
		# if random function picks 1, print tails
	counter += 1
	# increment loop by 1

# END OF PROGRM 

''' 
CS 131B LAB 2
Coin Toss
Purpose. Write a computer game program, from scratch, using if-logic and count-controlled loops.
Pretend that you have been hired by the National Football League (NFL) to write a program to replace the coin toss. 
The output should be simple: either the word "Heads" or the word "Tails". Allow the user to specify (via keyboard data entry) the number of coin tosses to perform when you run the program, and have the program display the result of each coin toss (that is, "Heads" or "Tails").

Read about "randomizing" here before you begin writing your program:
Gaming.supplemental.pdf
Preview the document

Here's the algorithm you should use:
============================
Have the user to enter how many coin tosses to perform
Input and store the user's value for how many coin tosses to perform
Create a counter variable and set it to zero

Start the loop here          
          If the counter variable equals the number of tosses to perform               
                       Break from the loop          
          Get and store a randomly-generated number in the range 0 to 1          
          If the randomly-generated number equals 0               
                       Output "heads"          
          If the randomly-generated number equals 1               
                       Output "tails"          
         Add one to the counter variable
Loop back from here
============================

Example running of the program with user input in bold:
(you do not need to have your program print out in bold, bold is just used to make the user input easier to see in this lab description)

Enter the number of tosses to perform:  3
Heads
Tails
Heads

'''
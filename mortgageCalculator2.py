# -*- coding: utf-8 -*-
# @Author: sabrina
# @Date:   2019-09-11 19:35:16
# @Last Modified by:   sabrina
# @Last Modified time: 2019-10-14 22:44:01

import math

def mortgageCalculator(borrowed, intRate, payback):
	"calculation from mortgage formula"

	# converts yearly annual interest rate and payback period (given in years) to monthly rate and period
	intRate /= 100 * 12
	payback *= 12

	monthly = (borrowed * math.pow((1 + intRate), payback) * intRate) / (math.pow((1 + intRate),payback) - 1)

	return monthly


if __name__ == '__main__':

	# create and open file `mortgageOutput.txt` to write (w) output
	filename = open("mortgageOutput.txt", "w")

	# takes user input and converts to corresponding data type for formula
	amountBorrowed = int(input("Enter the amount borrowed. Press the enter key to continue.\n"))
	annualIntRate = float(input("Enter annual interest rate. Press the enter key to continue.\n"))
	paybackPeriod = int(input("Enter payback period. Press the enter key to continue.\n"))

	# function to calculate mortgage
	monthlyPayment = mortgageCalculator(amountBorrowed, annualIntRate, paybackPeriod)

	# using string formatting, write to file user input variables and calculated result.
	filename.write("%s%d\n" % ("Amount Borrowed: $", amountBorrowed))			# %s - string, %d - integer
	filename.write("%s%f%s\n" % ("Annual Interest Rate: ", annualIntRate, "%"))	# %f - float
	filename.write("%s%d %s\n" % ("Payback Period: ", paybackPeriod, "Years"))
	filename.write("%s%.2f\n" % ("Monthly Payment: $", monthlyPayment))			# %.2f - 2 decimal float

	# close file when finished
	filename.close()

# END OF PRGRAM
'''
Notes:
input() functions read data from the keyboard as string

`file object = open(file_name [, access_mode][, buffering])` creates a FILE object that can be utilized to call other methods
	- file_name: name of the file to access
	- access_mode: determines the mode in which the file has to be opened (read, write, append, etc.) - default set to read (r)
	- buffering: 0 - no buffering takes place, 1 - line buffering is performed while accessing a file, >1 - performed with indicated buffer size
** PARAMETERS IN STRING FORMAT

`fileObject.close()` flushes any unwritten information and closes the file object - no more writing can be done

`fileObject.write(string)` writes any string to an open file. DOESNT ADD NEWLINE ('\n') TO END OF STRING
	** python strings can have binary data and not just text

`fileObject.read([count])` reads a string from an open file
	** python strings can have binary data apart from text data
	- [count]: number of bytes to be read from the opened file; reads from the beginning of the file - if [count] is mission, then it tries to read as much as possible (until EOF??)

Purpose:  Use files in Python

Lab

In this lab you will be performing much of the same logic from Lab 1.  You are to use most of Lab 1's logic, and you will modify the logic to print the output of the program to the following output file:

	mortgageOutput.txt

Name the program source code file mortgageCalculator2.py and submit the required file here in Canvas. 

Here are the program specifications:
1. Choose a dollar amount to be borrowed, as a whole number.

2. Specify an annual percent interest rate, as a floating-point number.

3. Calculate the monthly payment in dollars, as a floating-point number, using the formula shown below:
	(p * (1 + r)n * r) / ((1 + r)n - 1)

	• p is the mortgage amount as entered by the user
	• r is the monthly decimal interest rate
	• n is the number of monthly payments in the payback period


4. Include in the output an echo of the input amount borrowed, the annual percent interest rate (without formatting) and the payback period (in years).  Make sure you write the output to the output file this time and not to the console screen.

5. Include in the output the calculated monthly payment, formatted to show two decimal places (like this: 1000.00) Here's how to calculate a mortgage payment: • p is the mortgage amount as entered by the user • r is the monthly decimal interest rate • n is the number of monthly payments in the payback period.  Make sure you write the output to the output file this time and not to the console screen.
 

Program I/O --

Input: 3 programmer-specified inputs (amount borrowed, interest rate, and 30 year payback period) Output: Echoes of each input and the calculated monthly payment. Example.

For example:
	Amount borrowed (programmer input) = $270000
	Annual interest rate (programmer input) = 5.125%
	Payback period (programmer input) = 30 Years
	Monthly payment (calculated output) = $1470.11

All of these lines of output should be written to the output file and not to the console window.
'''
# -*- coding: utf-8 -*-
# @Author: Sabrina
# @Date:   2019-08-20 09:58:31
# @Last Modified by:   sabrina
# @Last Modified time: 2019-08-28 12:59:53

import math

amountBorrowed = int(input("Enter the amount borrowed. Press the enter key to continue.\n"))
annualIntRate = float(input("Enter annual interest rate. Press the enter key to continue.\n"))
paybackPeriod = int(input("Enter payback period. Press the enter key to continue.\n"))
# takes user input and converts to corresponding data type for formula

	# amountBorrowed = 270000
	# annualIntRate = 5.125 / 100 /12
	# paybackPeriod = 30 * 12


print("Amount Borrowed: $", amountBorrowed)
print("Annual Interest Rate: ", annualIntRate, "%")
print("Payback Period: ", paybackPeriod, "Years")

annualIntRate /= 100 * 12
paybackPeriod *= 12
# converts yearly annual interest rate and payback period (given in years) to monthly rate and period

# monthlyPayment = (amountBorrowed * ((1 + annualIntRate) ** paybackPeriod) * annualIntRate) / (((1 + annualIntRate) ** paybackPeriod) - 1)
# calculation from mortgage formula
# ** calculates the power of something

monthlyPayment = (amountBorrowed * math.pow((1 + annualIntRate), paybackPeriod) * annualIntRate) / (math.pow((1 + annualIntRate),paybackPeriod) - 1)
# equivalence to use `import math	` math.pow(value, to the power)`

monthlyPayment = "%.2f" % monthlyPayment
# to two decimal places

print("Monthly Payment: $", monthlyPayment)

# END OF PROGRAM

# CS 131B LAB 1
# Here are the program specifications:
# 1. Choose a dollar amount to be borrowed, as a whole number.
# 2. Specify an annual percent interest rate, as a floating-point number.
# 3. Calculate the monthly payment in dollars, as a floating-point number, using the formula shown below:
# 	(p * (1 + r)^n * r) / ((1 + r)^n - 1)
# 	• p is the mortgage amount as entered by the user
# 	• r is the monthly decimal interest rate
# 	• n is the number of monthly payments in the payback period
# 4. Include in the output an echo of the input amount borrowed, the annual percent interest rate (without formatting) and the payback period (in years).
# 5. Include in the output the calculated monthly payment, formatted to show two decimal places (like this: 1000.00) Here's how to calculate a mortgage payment: • p is the mortgage amount as entered by the user • r is the monthly decimal interest rate • n is the number of monthly payments in the payback period

# Program I/O --
# Input: 3 programmer-specified inputs (amount borrowed, interest rate, and 30 year payback period) 
# Output: Echoes of each input and the calculated monthly payment. Example.
# For example:
# Amount borrowed (programmer input) = $270000
# Annual interest rate (programmer input) = 5.125%
# Payback period (programmer input) = 30 Years
# Monthly payment (calculated output) = $1470.11

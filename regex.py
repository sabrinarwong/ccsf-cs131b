# -*- coding: utf-8 -*-
# @Author: sabrina
# @Date:   2019-09-11 19:37:21
# @Last Modified by:   sabrina
# @Last Modified time: 2019-10-27 23:10:14

import re

def regex1(string):
	'(1) a regular expression that matches something that has one or more lowercase letters'

	re.match()


def regex2(string):
	'(2) a regular expression that matches something that has one or more uppercase letters'
	


def regex3(string):
	'(3) a regular expression that matches something that has one or more digits (that is, 0, 1, 2, 3, 4, 5, 6, 7, 8, or 9).'

# If a regular expression matches something in the string, print out a statement saying that the regular expression matches something in the string.  If a regular expression does not match something in the string, print out a statement saying that the regular expression does not match something in the string.
if __name__ == '__main__':
	string1 = "A man a plan a canal panama".
	string2 = "ALPHA BRAVO CHARLIE DELTA ECHO FOXTROT"
	string3 = "alphabravocharliedeltaechofoxtrot"
	string4 = "0123456789"

	regex1(string1)
	regex2(string1)
	regex3(string1)

	regex1(string2)
	regex2(string2)
	regex3(string2)

	regex1(string3)
	regex2(string3)
	regex3(string3)

	regex1(string4)
	regex2(string4)
	regex3(string4)


# END OF PROGRAM
'''

NOTES:
A regular expression is a special sequence of characters that helps you MATCH OR FIND OTHER STRINGS OR SETS OF STRINGS, using a specialized syntax held in a pattern.

	`import re` 

Useful expression and matches:
	- [literal characters themselves]
	- . (matches any character except \n)
	- \w (letter or number or _), \w (else)
	- \s (whitespace character), \S (any whitespace)
	- \d (decimal digit)
	- ^ (start of string)
	- $ (end of string)

Flags:
	- ASCII , A
	- DOTALL, S
	- IGNORECASE, I
	- LOCALE, L
	- MULTILINE, M
	- VERBOSE, X






CS131B LAB 9
Purpose:  To make and use regular expressions.

Lab

In this lab you will have 4 strings that will be searched to see if they match some regular expressions.

The 4 strings you are to use are: 

	string1 = "A man a plan a canal panama".
	string2 = "ALPHA BRAVO CHARLIE DELTA ECHO FOXTROT"
	string3 = "alphabravocharliedeltaechofoxtrot"
	string4 = "0123456789"

Each string should be tested using regular expressions.  Each string should use a re object to see if it matches

	(1) a regular expression that matches something that has one or more lowercase letters
	(2) a regular expression that matches something that has one or more uppercase letters
	(3) a regular expression that matches something that has one or more digits (that is, 0, 1, 2, 3, 4, 5, 6, 7, 8, or 9).

You may make one or more re objects for (1) - (3).

If a regular expression matches something in the string, print out a statement saying that the regular expression matches something in the string.  If a regular expression does not match something in the string, print out a statement saying that the regular expression does not match something in the string.


Program I/O --

	Output: Displays sentences saying if a given string matches a regular expression.

	For example:

		string1 matches a regular expression that indicates it has lowercase letters

		string1 matches a regular expression that indicates it has uppercase letters

		string1 does not match a regular expression that indicates it has digits

		string2 does not match a regular expression that indicates it has lowercase letters

		string2 matches a regular expression that indicates it has uppercase letters

		string2 does not match a regular expression that indicates it has digits

		... etc.
'''
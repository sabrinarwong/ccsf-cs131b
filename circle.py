# -*- coding: utf-8 -*-
# @Author: sabrina
# @Date:   2019-09-29 22:15:17
# @Last Modified by:   sabrina
# @Last Modified time: 2019-09-29 22:15:36
# Purpose:  To get more experience working with object oriented programming using a programmer defined class.

# Lab

# Write a simple class named Circle, with three private variables members:  numbers named x, y and radius.  The center of the circle is denoted by coordinates (x,y), and the radius of the circle is denoted by radius.  The Circle class should be written to have methods that use these def statements:

# def setRadius(r)
# def setX(value)
# def setY(value)
# def getRadius()
# def getX()
# def getY()
# def getArea()
# def containsPoint(xValue, yValue)
# Here's descriptions of what the methods should do:

# setRadius(r)

# Takes the radius of the circle as the numeric r parameter, and assigns the private variable radius to the value of r.

# setX(value)

# Takes the numeric value parameter, and assigns the private variable x to be equal to value.

# setY(value)

# Takes the numeric value parameter, and assigns the private variable x to be equal to value.

# getRadius()

#               Returns the value of the private variable radius.

# getX()

# Returns the value of the private variable x.

# getY()

# Returns the value of the private variable y.

# getArea()

# Takes the radius of the circle as the numeric r parameter, and returns a number that represents the area of the circle.  When you are calculating the area you can use 3.14 for pi.  The formula is:  radius * radius * pi.  

# containsPoint(xValue, yValue)

# Returns the value True if the point given by the numeric xValue and yValue parameters is contained in the circle, and returns False if not.  You can determine whether or not a point is in a circle by calculating the distance from the center of the circle (its x and y coordinates) to the point (parameters xValue, yValue).  If this distance is less than or equal to the radius then the point is inside the circle.  For your reference, here is how to calculate distance between two points (Links to an external site.).  

# For example, let's say we have a Circle object named myCircle which has x=2.0, y=3.0, and radius=2.0.  

# myCircle.containsPoint(2.0, 4.0) should return true because (2.0, 4.0) is contained in myCircle.  
# myCircle.containsPoint(2.0, 10.0) should return false because (2.0, 10.0) is not contained in myCircle.
 

# Write a function named main that tests your class. Main should instantiate a number of circle objects with different radius values and centers.  You should test all your methods until you are confident that they work.  At minimum, make sure you try each of the following and provide sample output for each:

# Create a circle object and set its x, y, and radius. Verify that its area is calculated correctly.
# Set the circle object's x, y, and radius values to new values.
# Verify that your containsPoint() function works by trying a point which is in fact in the circle represented by your circle object, and showing it returns true.  Also, try a different point which is not in your circle and show it returns false.
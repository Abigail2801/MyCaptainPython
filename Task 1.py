#Task 1 : WAP which accepts the radius of the circle from the user and computes area

from math import pi #importing the pi from the math module in python
rad = float(input("Enter the Radius of circle: \n"))#Taking the radius from the user

area = pi * rad * rad
print("The area of the circle with radius",rad,"is: \n",area)

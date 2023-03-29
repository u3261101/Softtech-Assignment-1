'''
Author: Akhil Prasad
Date created: 29/03/23
Date changed: 29/03/23

This program 

Input:

Output:

'''

#Asks for user input, goes through the formula and prints the YTM
#Includes error validation included to avoid users typing letters to crash the program
def main():
    initialHeight = float(input("Enter initial height (in meters): "))
    coefficientOfRestitution = float(input("Enter coefficient of restitution (0-1): "))
    newHeight = initialHeight * coefficientOfRestitution 
    numberOfBounces = 1
    distanceTravelled = initialHeight

    while newHeight > 0.1:
        numberOfBounces += 1
        distanceTravelled += 2 * newHeight
        newHeight *= coefficientOfRestitution
        

    print(distanceTravelled)
    print(numberOfBounces)


main()
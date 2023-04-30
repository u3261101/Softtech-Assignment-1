'''
Author: Akhil Prasad
Date created: 29/03/23
Date changed: 29/03/23

This program asks the user to input starting height and the restitution of a ball 
to calculate the maximum number of bounces before it rises to a height of less than 10 cm,
and the total distance travelled by the ball in meters

Input:
Initial height
Coefficient of restitution

Output:
Number of bounces
Total distance travelled

'''

#asks the user for input and calculates the number of  bounces and the total distance travelled
def main():
    userChoice = menu()

    if userChoice == "A":
        bouncingBallCalculator()
        main()
        

#gets user coefficient and uses error validation to correct user misinputs
def coefficient(coefficientsOfBalls):
    coefficientOfRestitution = (input('''
Enter coefficient of restitution or one of the following options: 
------------------------
tennis ball
basket ball
super ball
soft ball
------------------------
Please enter: ''')).lower()

    try:
        coefficientOfRestitution = coefficientsOfBalls[coefficientOfRestitution]
    
    except KeyError:
        coefficientOfRestitution = float(coefficientOfRestitution)
    
    return coefficientOfRestitution


#calcualtes the height after bounce
def height(initialHeight, coefficientOfRestitution):

    height = initialHeight * coefficientOfRestitution

    return height


#Calculates the total distance travelled
def distance(initialHeight,coefficientOfRestitution, MINIMUM_HEIGHT_FOR_BALL ):
    
    newHeight = height(initialHeight, coefficientOfRestitution)

    distanceTravelled = initialHeight
    
    while newHeight > MINIMUM_HEIGHT_FOR_BALL:
        #2 times height as the ball travels up and down
        distanceTravelled += 2 * newHeight
        newHeight *= coefficientOfRestitution

    return distanceTravelled


#calculates the number of bounces depending on the ball  
def bounce(initialHeight,coefficientOfRestitution, MINIMUM_HEIGHT_FOR_BALL):
    
    newHeight = height(initialHeight, coefficientOfRestitution)
    
    numberOfBounces = 1
    
    while newHeight > MINIMUM_HEIGHT_FOR_BALL:
        numberOfBounces += 1
        newHeight *= coefficientOfRestitution
    
    return numberOfBounces


#displays meny listings
def menu():
    print(f'''
    A: Bouncing ball Calculator
    B: Exit
    ''')

    choice = input("Please enter A or B:  ")
    return choice


#uses multiple functions to calculate and display total distance travelled and number of bounces 
def bouncingBallCalculator():
    TENNIS_BALL_COEFFICIENT = 0.7
    BASKET_BALL_COEFFICIENT = 0.75
    SUPER_BALL_COEFFICIENT = 0.9
    SOFT_BALL_COEFFICIENT = 0.3
    MINIMUM_HEIGHT_FOR_BALL = 0.1

    coefficientsOfBalls = {
        "tennis ball" : TENNIS_BALL_COEFFICIENT, 
        "basket ball" : BASKET_BALL_COEFFICIENT, 
        "super ball" : SUPER_BALL_COEFFICIENT, 
        "soft ball": SOFT_BALL_COEFFICIENT
        }
    
    initialHeight = float(input("Enter initial height (in meters): "))
    
    coefficientOfRestitution = coefficient(coefficientsOfBalls)

    distanceTravelled = distance(initialHeight, coefficientOfRestitution, MINIMUM_HEIGHT_FOR_BALL)

    numberOfBounces = bounce(initialHeight, coefficientOfRestitution, MINIMUM_HEIGHT_FOR_BALL)
    
    print(f'''
Coefficient:                                    {coefficientOfRestitution}
    
Total distance travelled (in meters):           {round(distanceTravelled,2)}

Total number of bounces:                        {numberOfBounces}

-------------------------------------------------------------------------------
    ''')


main()
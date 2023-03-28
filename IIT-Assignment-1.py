'''
Author: Akhil Prasad
Date created: 28/03/23
Date changed: 28/03/23

This program calculates the YTM based on the user input of 
        face value, market value, 
        interest rate and years of maturity

Input:
Face value of bond: 
Coupon interest rate: 
Current market price: 
Years until maturity: 

Output:
Approximate YTM

'''

#Asks for user input, goes through the formula and prints the YTM
#Includes error validation included to avoid users typing letters to crash the program
def main():
    while True:
        try:
            value = float(input("Enter the face value of bond: "))
            interest = float(input("Enter the coupon interest rate: "))
            price = float(input("Enter the current market price: "))
            years = float(input("Enter the years until maturity: "))
 
        #if the user types characters, print a statement and restart the loop
        except ValueError:
            print("Please enter a number")

        else:
            intr = calc_intr(interest, value)
            a = calc_a(value, price, years)
            b = calc_b(value, price)
            ytm = round(calc_YTM(a, b, intr),2)

            print(f'Approximate YTM = {ytm}%')
            

#calculates interest rate for the YTM formula based on user input
def calc_intr(int, faceValue):
    intr = int*faceValue
    
    return intr


#calculates the value for a for the YTM formula based on user input
def calc_a(faceValue, currentPrice, yrsTillMaturity):
    a = (faceValue - currentPrice) / yrsTillMaturity
    
    return a


#calculates the value for b for the YTM formula based on user input
def calc_b(faceValue, curentPrice):
    b = (faceValue + curentPrice) / 2

    return b


#calculates YTM based on the values of a, b and intr
def calc_YTM(a,b, intr):
    #multiplied by 100 to make percentage easier to read
    ytm = ((intr + a) / b ) * 100
    
    return ytm


main()
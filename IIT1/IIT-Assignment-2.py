'''
Author: Akhil Prasad
Date created: 7/5/23
Date changed: 7/5/23

This program calculates available weight for astronauts 
based on the celestial body they are travelling to


output:
avaliable weight per astronaut
avaliable weight of all astronauts
average avaliable weight of all astronauts
average avaliable weight of all astronauts on chosen planet

display:
outputs
planet
planet multiplier

use:
1. Use the Grid element [5 marks]
2. Add Label elements throughout your GUI. [5 marks]
3. Use the Background Colour property. [5 marks]
4. Allow a user to select choices from an either list box, drop-down menu, or scroll-down menu
element. [10 marks]
5. Allow a user to input the data using an entry widget. [10 marks]
6. Output data using an entry widget. [5 marks]
7. Allow a user to click on a Calculate button that triggers any calculation. [5 marks]
8. Allow a user to press an Exit or Quit button to properly close the program. [5 marks]
9. GUI Design. Is it simple to use and easy to understand? [5 marks]
10. Program is written using well-defined functions. [5 marks]
11. Program code layout. Separate blocks of code by a blank line. [2 marks]
12. The program must have an introduction (about the module, not the topic). Check style against
the Python style guide attached below. [2 marks]
13. Business rules are met. That is, your code solves the problem you are proposing (or at least
contributes to its solution). [6 marks]
'''
import tkinter

celestial_body = {
"mercury": 0.378,
"venus": 0.907,
"moon": 0.166,
"earth": 1,
"mars": 0.377,
"io": 0.1835,
"europa": 0.1335,
"ganymede": 0.1448,
"callisto": 0.1264
}

max_weight = {
    "c" : 100,
    "s": 150
}
def planet():
    while True:
        try:
            planetvalue = float(celestial_body[(input("Please enter the name of your destination: ")).lower()])
            return planetvalue
        except ValueError:
            print("Please enter a valid name")

def weight():
    while True:
        try:
            weightvalue = abs(float(input("Please enter the amount of weight you are carrying: ").lower()))
            return weightvalue
        except ValueError:
            print("Please enter a valid number")

def typeOfCrew():
    while True:
        try:
            max_weight_allowed = float(max_weight[input("Please enter your postion (crew or specialist): ")])
            return max_weight_allowed
        except ValueError:
            print("Please enter a valid name")


planetvalue = planet()
weights = []
max_weights_allowed = []

for i in range(6):
    weightvalue = weights.append(weight())   
    max_weight_allowed = max_weights_allowed.append(typeOfCrew())

print(weights, "current weights")
print(max_weights_allowed, "max_weights_allowed")    

available_weight = []
#available weight
for i in range(len(weights)):
    available = max_weights_allowed[i] - weights[i]
    available_weight.append(available)

#average available weight
sum_available_weight = sum(available_weight)
available_average = str(sum_available_weight/len(available_weight))
print(available_weight, "available_weight for each astronaut")

#equivalent average on destination
for i in range(len(available_weight)):
    dest_available_average = str((sum_available_weight* planetvalue)/len(available_weight))

print((available_average), "average available weight")
print((dest_available_average), "average available weight on planet")

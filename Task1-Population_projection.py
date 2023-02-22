'''
The ABS projections on POPULATION is based on the following assumptions:
One birth every 7 seconds
One death every 13 seconds
One new immigrant every 45 seconds
Write a program  (GUI program) to display the POPULATION for each of the next five years. Use the 
current Australian POPULATION and that one year has 365 days.

Input : Amount of years to predict POPULATION for
Process :
----------------
Count POPULATION growth per minute
multiply it by minutes per year
----------------
Output : Total POPULATION after certain amount of years
'''
import tkinter
class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("ABS Australian Population Calculator")
        POPULATION = 26277169
        MINUTES_PER_YEAR = 60*24*365
        BIRTHS_PER_YEAR = 60/7 * MINUTES_PER_YEAR
        DEATHS_PER_YEAR = 60/13 * MINUTES_PER_YEAR
        IMMIGRATIONS_PER_YEAR = 60/45 * MINUTES_PER_YEAR
        Years = 0

# runs until year 5, calculating the end population based on the current year in each instance and displaying it using the tkinter module
        while Years<=5:
            End_Population = POPULATION+((((IMMIGRATIONS_PER_YEAR+BIRTHS_PER_YEAR)-DEATHS_PER_YEAR)*Years))
            self.label2 = tkinter.Label(self.main_window, text = f'Year {Years}: {int(End_Population):,}')
            Years+=1
            self.label2.pack()
        tkinter.mainloop()


my_gui = myGUI()




'''
def main():
    ...

if __name__ == "__main__":
    main()
'''
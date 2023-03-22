'''
There are three seating categories at a stadium. Class A seats cost $20, Class B 
seats cost $15, and Class C seats cost $10. Write a program (a  GUI program) that 
asks how many tickets for each class of seats were sold, then displays the amount 
of income generated from ticket sales
'''

import tkinter
from tkinter import simpledialog

class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Stadium Seating Revenue Calculation Tool ")

        #create frames
        self.class_A_frame = tkinter.Frame()
        self.class_B_frame = tkinter.Frame()
        self.class_C_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()
        self.result_frame = tkinter.Frame()

        #create label and entry
        self.class_A_label = tkinter.Label(self.class_A_frame, text = "Class A tickets sold ($20 each): ")
        self.class_A_entry = tkinter.Entry(self.class_A_frame)
        self.class_B_label = tkinter.Label(self.class_B_frame, text = "Class B tickets sold ($15 each): ")
        self.class_B_entry = tkinter.Entry(self.class_B_frame)
        self.class_C_label = tkinter.Label(self.class_C_frame, text = "Class C tickets sold ($10 each): ")
        self.class_C_entry = tkinter.Entry(self.class_C_frame)
        
        #create buttons
        display_button = tkinter.Button(self.button_frame, text = "Calculate", command= self.display)
        quit_button = tkinter.Button(self.button_frame, text = "Quit", command= self.main_window.destroy)

        #create text box
        self.results_tb = tkinter.Text(self.result_frame, bg='lightblue')

        #pack labels, entry, buttons and text box
        self.class_A_label.pack(side='left')
        self.class_A_entry.pack(side='left')
        self.class_B_label.pack(side='left')
        self.class_B_entry.pack(side='left')
        self.class_C_label.pack(side='left')
        self.class_C_entry.pack(side='left')
        display_button.pack(side='left')
        quit_button.pack(side='left')
        self.results_tb.pack()

        #pack frames
        self.class_A_frame.pack()
        self.class_B_frame.pack()
        self.class_C_frame.pack()
        self.button_frame.pack()
        self.result_frame.pack()
        
        #Enter the tkinter main loop
        tkinter.mainloop()

    #take user input and display the result
    def display(self):
        #clear the text box
        self.results_tb.delete('1.0', 'end')
        result_string = ""
        
        #price per seating category
        A_PRICE = 20
        B_PRICE = 15
        C_PRICE = 10

        #store the amount of seats sold
        A_tickets = float(self.class_A_entry.get())
        B_tickets = float(self.class_B_entry.get())
        C_tickets = float(self.class_C_entry.get())

        #find the total by multiplying tickets sold by the price for each ticket
        Total = A_tickets * A_PRICE + B_tickets * B_PRICE + C_tickets * C_PRICE

        #display result
        result_string = f'Total income generated was ${Total}'
        self.results_tb.insert('1.0', result_string)

my_gui = myGUI()
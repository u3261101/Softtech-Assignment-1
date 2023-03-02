'''
A company has determined that its annual profit is typically 23 percent of total sales. Write a 
Python program (GUI App) that asks the user to enter the projected amount of total sales, 
then displays the profit that will be made from that amount. Hint: Use the value 0.23 to 
represent 23 percent

'''

import tkinter
class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Profit Calculator")

        #create frames
        self.input_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()
        self.result_frame = tkinter.Frame()

        #create label and entry
        self.Sales_label = tkinter.Label(self.input_frame, text = "Enter projected amount of total sales: ")
        self.Sales_entry = tkinter.Entry(self.input_frame)
        
        #create buttons
        calculate_button = tkinter.Button(self.button_frame, text = "Calculate Profits", command= self.calculate)
        quit_button = tkinter.Button(self.button_frame, text = "Quit", command= self.main_window.destroy)

        #create text box
        self.results_tb = tkinter.Text(self.result_frame)

        #pack labels, entry, buttons and text box
        self.Sales_label.pack(side='left')
        self.Sales_entry.pack(side='left')
        calculate_button.pack(side='left')
        quit_button.pack(side='left')
        self.results_tb.pack()

        #pack frames
        self.input_frame.pack()
        self.button_frame.pack()
        self.result_frame.pack()
        
        #Enter the tkinter main loop
        tkinter.mainloop()

    #take user input and display the result
    def calculate(self):
        result_string = ""

        #clears the text box every time new entrys are displayed
        self.results_tb.delete('1.0', tkinter.END)

        sales = float(self.Sales_entry.get())
        sales = sales*0.23
        result_string = f"Profit: ${sales}"
        self.results_tb.insert('1.0', result_string)

my_gui = myGUI()
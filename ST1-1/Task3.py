'''
Write  a  GUI program  for  calculating  the  quiz  mark  for  ST1  unit.  The  program 
should read four inputs as quiz mark for each quiz, save it as integers, and calculator the sum 
of four quiz marks and display the sum. A test run of the working program is as shown below:
'''

import tkinter
class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("ST1 Quiz Mark Calculator")

        #create frames
        self.Quiz1_frame = tkinter.Frame()
        self.Quiz2_frame = tkinter.Frame()
        self.Quiz3_frame = tkinter.Frame()
        self.Quiz4_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()
        self.result_frame = tkinter.Frame()

        #create label and entry
        self.Quiz1_label = tkinter.Label(self.Quiz1_frame, text = "Enter quiz 1 marks(out  of 10) ")
        self.Quiz1_entry = tkinter.Entry(self.Quiz1_frame)
        self.Quiz2_label = tkinter.Label(self.Quiz2_frame, text = "Enter quiz 2 marks(out  of 10) ")
        self.Quiz2_entry = tkinter.Entry(self.Quiz2_frame)
        self.Quiz3_label = tkinter.Label(self.Quiz3_frame, text = "Enter quiz 3 marks(out  of 10) ")
        self.Quiz3_entry = tkinter.Entry(self.Quiz3_frame)
        self.Quiz4_label = tkinter.Label(self.Quiz4_frame, text = "Enter quiz 4 marks(out  of 10) ")
        self.Quiz4_entry = tkinter.Entry(self.Quiz4_frame)
        
        #create buttons
        display_button = tkinter.Button(self.button_frame, text = "Calculate Sum", command= self.display)
        quit_button = tkinter.Button(self.button_frame, text = "Quit", command= self.main_window.destroy)

        #create text box
        self.results_tb = tkinter.Text(self.result_frame, bg='lightblue')

        #pack labels, entry, buttons and text box
        self.Quiz1_label.pack(side='left')
        self.Quiz1_entry.pack(side='left')
        self.Quiz2_label.pack(side='left')
        self.Quiz2_entry.pack(side='left')
        self.Quiz3_label.pack(side='left')
        self.Quiz3_entry.pack(side='left')
        self.Quiz4_label.pack(side='left')
        self.Quiz4_entry.pack(side='left')
        display_button.pack(side='left')
        quit_button.pack(side='left')
        self.results_tb.pack()

        #pack frames
        self.Quiz1_frame.pack()
        self.Quiz2_frame.pack()
        self.Quiz3_frame.pack()
        self.Quiz4_frame.pack()
        self.button_frame.pack()
        self.result_frame.pack()
        
        #Enter the tkinter main loop
        tkinter.mainloop()

    #take user input and display the result
    def display(self):
        result_string = ""

        #clears the text box every time new entrys are displayed
        self.results_tb.delete('1.0', tkinter.END)
        
        Quiz1 = self.Quiz1_entry.get()
        Quiz2 = self.Quiz2_entry.get()
        Quiz3 = self.Quiz3_entry.get()
        Quiz4 = self.Quiz4_entry.get()

        if Quiz1.isnumeric() and Quiz2.isnumeric() and Quiz3.isnumeric() and Quiz4.isnumeric():
            Quiz1 = int(Quiz1)
            Quiz2 = int(Quiz2)
            Quiz3 = int(Quiz3)
            Quiz4 = int(Quiz4)
            Total = Quiz1+Quiz2+Quiz3+Quiz4     
            result_string = f"The quiz marks for ST1 unit is {Total}"
        else:
            result_string = f"please enter a number"
        

        self.results_tb.insert('1.0', result_string)

my_gui = myGUI()

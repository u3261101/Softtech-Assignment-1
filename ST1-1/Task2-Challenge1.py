'''
Write a Python program (GUI App) that requests the following information from user and 
displays it: 
Student name
Student address, with suburb, state, and post code
Student telephone number 
Student Course

'''

import tkinter
class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Student info")

        #create frames
        self.name_frame = tkinter.Frame()
        self.address_frame = tkinter.Frame()
        self.number_frame = tkinter.Frame()
        self.course_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()
        self.result_frame = tkinter.Frame()

        #create label and entry
        self.name_label = tkinter.Label(self.name_frame, text = "Student name")
        self.name_entry = tkinter.Entry(self.name_frame)
        self.address_label = tkinter.Label(self.address_frame, text = "Student address (include suburb, state, and post code)")
        self.address_entry = tkinter.Entry(self.address_frame)
        self.number_label = tkinter.Label(self.number_frame, text = "Student telephone number")
        self.number_entry = tkinter.Entry(self.number_frame)
        self.course_label = tkinter.Label(self.course_frame, text = "Student course")
        self.course_entry = tkinter.Entry(self.course_frame)
        
        #create buttons
        display_button = tkinter.Button(self.button_frame, text = "Display", command= self.display)
        quit_button = tkinter.Button(self.button_frame, text = "Quit", command= self.main_window.destroy)

        #create text box
        self.results_tb = tkinter.Text(self.result_frame)

        #pack labels, entry, buttons and text box
        self.name_label.pack(side='left')
        self.name_entry.pack(side='left')
        self.address_label.pack(side='left')
        self.address_entry.pack(side='left')
        self.number_label.pack(side='left')
        self.number_entry.pack(side='left')
        self.course_label.pack(side='left')
        self.course_entry.pack(side='left')
        display_button.pack(side='left')
        quit_button.pack(side='left')
        self.results_tb.pack()

        #pack frames
        self.name_frame.pack()
        self.address_frame.pack()
        self.number_frame.pack()
        self.course_frame.pack()
        self.button_frame.pack()
        self.result_frame.pack()
        
        #Enter the tkinter main loop
        tkinter.mainloop()

    #take user input and display the result
    def display(self):
        result_string = ""

        #clears the text box every time new entrys are displayed
        self.results_tb.delete('1.0', tkinter.END)

        student_name = self.name_entry.get()
        student_address = self.address_entry.get()
        student_number = self.number_entry.get()
        student_course = self.course_entry.get()

        result_string = f" Student name: {student_name} \n Student address: {student_address} \n Student phone number: {student_number} \n Student Course: {student_course}"
        self.results_tb.insert('1.0', result_string)

my_gui = myGUI()
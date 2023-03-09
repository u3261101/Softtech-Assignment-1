'''
Write a GUI program that asks the user to enter the number of times that they have run around 
a racetrack, and then uses a loop to prompt them to enter the lap time for each of their laps. 
When the loop finishes, the program should display the time of their  fastest lap, the time of 
their slowest lap, and their average lap time
'''


import tkinter
from tkinter import simpledialog

class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Lap Timer Tool")

        #create frames
        self.lap_num_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()
        self.result_frame = tkinter.Frame()

        #create label and entry
        self.lap_num_label = tkinter.Label(self.lap_num_frame, text = "Enter the number of laps completed: ")
        self.lap_num_entry = tkinter.Entry(self.lap_num_frame)
        
        #create buttons
        display_button = tkinter.Button(self.button_frame, text = "Calculate", command= self.display)
        quit_button = tkinter.Button(self.button_frame, text = "Quit", command= self.main_window.destroy)

        #create text box
        self.results_tb = tkinter.Text(self.result_frame, bg='lightblue')

        #pack labels, entry, buttons and text box
        self.lap_num_label.pack(side='left')
        self.lap_num_entry.pack(side='left')
        display_button.pack(side='left')
        quit_button.pack(side='left')
        self.results_tb.pack()

        #pack frames
        self.lap_num_frame.pack()
        self.button_frame.pack()
        self.result_frame.pack()
        
        #Enter the tkinter main loop
        tkinter.mainloop()

    #take user input and display the result
    def display(self):
        #clear the text box
        self.results_tb.delete('1.0', 'end')
        
        result_string = ""

        num_of_laps = int(self.lap_num_entry.get())
        lap_times = []

        for num in range(num_of_laps):
            #get the user input and convert it into a float value
            lap_time = (simpledialog.askstring(title=f"Lap {num+1}", prompt=f"Enter time for lap {num+1}"))
            lap_time = float(lap_time)

            #add the entered value into the la_times list
            lap_times.append(lap_time)
            
            #allows the loop to end and next user input to be added to the lap_times list
            num_of_laps -=1

        #sort the lap_times list in ascending order
        lap_times.sort()  

        #calculate average using the sum method divided by the amount of values in lap_times list
        average = round(sum(lap_times)/len(lap_times),2)

        #display result
        result_string = f'''
        Fastest: {lap_times[len(lap_times)-1]}
        Slowest: {lap_times[0]}
        Average: {average}
        '''
        self.results_tb.insert('1.0', result_string)

my_gui = myGUI()
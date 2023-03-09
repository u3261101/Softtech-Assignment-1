'''
Write a GUI program that asks the user to enter the number of times that they have run around 
a racetrack, and then uses a loop to prompt them to enter the lap time for each of their laps. 
When the loop finishes, the program should display the time of their  fastest lap, the time of 
their slowest lap, and their average lap time
'''


import tkinter

class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Lap Timer Tool")


        num_of_laps = 0
        lap_times = []
        #create frames
        self.lap_num_frame = tkinter.Frame()
        self.lap_time_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()
        self.result_frame = tkinter.Frame()

        #create label and entry
        self.lap_num_label = tkinter.Label(self.lap_num_frame, text = "Enter the number of laps completed: ")
        self.lap_num_entry = tkinter.Entry(self.lap_num_frame)
        self.lap_time_label = tkinter.Label(self.lap_time_frame, text = f"Enter lap {num_of_laps} time: ")
        self.lap_time_entry = tkinter.Entry(self.lap_time_frame)
        
        #create buttons
        display_button = tkinter.Button(self.button_frame, text = "Calculate Sum", command= self.display)
        quit_button = tkinter.Button(self.button_frame, text = "Quit", command= self.main_window.destroy)

        #create text box
        self.results_tb = tkinter.Text(self.result_frame, bg='lightblue')

        #pack labels, entry, buttons and text box
        self.lap_num_label.pack(side='left')
        self.lap_num_entry.pack(side='left')
        self.lap_time_label.pack(side='left')
        self.lap_time_entry.pack(side='left')
        display_button.pack(side='left')
        quit_button.pack(side='left')
        self.results_tb.pack()

        #pack frames
        self.lap_num_frame.pack()
        self.lap_time_frame.pack()
        self.button_frame.pack()
        self.result_frame.pack()
        
        #Enter the tkinter main loop
        tkinter.mainloop()

    #take user input and display the result
    def display(self):
        # result_string = ""

        # #clears the text box every time new entrys are displayed
        # self.results_tb.delete('1.0', tkinter.END)

        # lap_num = int(self.lap_num_entry.get())
        # lap_time = int(self.lap_time_entry.get())
               

        # result_string = f"The quiz marks for ST1 unit is {...}"
        # self.results_tb.insert('1.0', result_string)
        num_of_laps = int(self.lap_num_entry.get())
        lap_times = []
        for num in range(num_of_laps):
            
            for time in range(lap_times):
                lap_time = (simpledialog.askstring(title="Student", prompt="S"))
                lap_time = float(lap_time)
                #(float(self.lap_time_entry.get())
                lap_times.append(lap_time)
                num_of_laps -=1

        lap_times.sort()  
        average = round(sum(lap_times)/len(lap_times),2)
        result_string = f'''
        Fastest: {lap_times[len(lap_times)-1]}
        Slowest: {lap_times[0]}
        Average: {average}
        '''
        self.results_tb.insert('1.0', result_string)
    # print(f"Fastest: {lap_times[len(lap_times)-1]}")
    # print(f"Slowest: {lap_times[0]}")
    # print(f"Average: {average}")

my_gui = myGUI()
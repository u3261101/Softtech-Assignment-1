'''
A nutritionist who works for a fitness club helps members by evaluating their diets. As part of her evaluation, 
she asks members for the number of fat grams and carbohydrate grams that they consumed in a day. Then, 
she calculates the number of calories that result from the fat, using the following formula: 
calories from fat =  fat grams x 3.9
Next, she calculates the number of calories that result from the carbohydrates, using the following formula: 
calories from carbs = carb grams x 4 
The nutritionist asks you to write a GUI program that will make these calculations
'''

import tkinter

class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Nutrition Tracker")

        #create frames
        self.fat_grams_frame = tkinter.Frame()
        self.carb_grams_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()
        self.result_frame = tkinter.Frame()

        #create label and entry
        self.fat_grams_label = tkinter.Label(self.fat_grams_frame, text = "Enter the number of fat grams consumed in one day: ")
        self.fat_grams_entry = tkinter.Entry(self.fat_grams_frame)
        self.carb_grams_label = tkinter.Label(self.carb_grams_frame, text = "Enter the number of carbohydrate grams consumed in one day: ")
        self.carb_grams_entry = tkinter.Entry(self.carb_grams_frame)
        
        #create buttons
        display_button = tkinter.Button(self.button_frame, text = "Calculate", command= self.display)
        quit_button = tkinter.Button(self.button_frame, text = "Quit", command= self.main_window.destroy)

        #create text box
        self.results_tb = tkinter.Text(self.result_frame, bg='lightblue')

        #pack labels, entry, buttons and text box
        self.fat_grams_label.pack(side='left')
        self.fat_grams_entry.pack(side='left')
        self.carb_grams_label.pack(side='left')
        self.carb_grams_entry.pack(side='left')
        display_button.pack(side='left')
        quit_button.pack(side='left')
        self.results_tb.pack()

        #pack frames
        self.fat_grams_frame.pack()
        self.carb_grams_frame.pack()
        self.button_frame.pack()
        self.result_frame.pack()
        
        #Enter the tkinter main loop
        tkinter.mainloop()

    #take user input and display the result
    def display(self):
        #clear the text box
        self.results_tb.delete('1.0', 'end')
        
        result_string = ""

        #get user input and store it using relative variables
        carb_grams = self.carb_grams_entry.get()
        fat_grams = self.fat_grams_entry.get()
        
        #Using constants to avoid magic numbers
        CRAB_MULTIPLIER = 4.0
        FAT_MULTIPLIER = 3.9

        #apply the formula provided
        if carb_grams.isnumeric() and fat_grams.isnumeric():
            carb_grams = float(self.carb_grams_entry.get())
            fat_grams = float(self.fat_grams_entry.get())
            carbs = carb_grams * CRAB_MULTIPLIER 
            fat =  fat_grams * FAT_MULTIPLIER
            total = carbs+fat
            #display result
            result_string = f'''
            Calories from carbs per day: {carbs}
            Calories from fat per day: {fat}
            Total calories: {total} kJ       
            '''
        else:
            result_string = f'''
        Please enter a numeric value
        '''
        
        self.results_tb.insert('1.0', result_string)


        

my_gui = myGUI()
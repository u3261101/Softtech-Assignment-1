import tkinter as tk

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
    "crew": 100,
    "specialist": 150
}

def calculate():
    planet_value = celestial_body[planet_var.get().lower()]
    weights = []
    max_weights_allowed = []
    for i in range(6):
        weights.append(abs(float(weight_entries[i].get())))
        max_weights_allowed.append(max_weight[crew_var.get()])

    available_weight = []
    # available weight
    for i in range(len(weights)):
        available = max_weights_allowed[i] - weights[i]
        available_weight.append(available)

    # average available weight
    sum_available_weight = sum(available_weight)
    available_average = str(round(sum_available_weight / len(available_weight), 2))
    # equivalent average on destination
    dest_available_average = str(round((sum_available_weight * planet_value) / len(available_weight), 2))

    # available weight for each astronaut
    for i in range(len(available_weight)):
        available_weight_str = available_entry.insert(0,available_weight[i])
    #available_weight_str = "\n".join([f"Available Weight for Astronaut {i+1}: {round(available_weight[i], 2)}" for i in range(len(available_weight))])

    result_label.config(text=f"Average Available Weight: {available_average}\nAverage Available Weight on Planet: {dest_available_average}\n{available_weight_str}")


# create the main window
window = tk.Tk()
window.title("Weight Calculator")

# create the planet selection label and dropdown menu
planet_label = tk.Label(window, text="Select a Destination Planet:")
planet_label.grid(row=0, column=0, padx=10, pady=10)
planet_var = tk.StringVar(value=list(celestial_body.keys())[0])
planet_dropdown = tk.OptionMenu(window, planet_var, *celestial_body.keys())
planet_dropdown.grid(row=0, column=1, padx=10, pady=10)

# create weight input labels and entry boxes
weight_labels = []
weight_entries = []
available_labels = []
available_entries = []
for i in range(6):
    weight_labels.append(tk.Label(window, text=f"Enter Weight {i+1}:"))
    weight_labels[i].grid(row=i+1, column=0, padx=10, pady=10)
    weight_entries.append(tk.Entry(window))
    weight_entries[i].grid(row=i+1, column=1, padx=10, pady=10)

    # create crew type dropdown for each weight entry
    crew_var = tk.StringVar(value=list(max_weight.keys())[0])
    crew_dropdown = tk.OptionMenu(window, crew_var, *max_weight.keys())
    crew_dropdown.grid(row=i+1, column=3, padx=10, pady=10)

    # create crew label for each weight entry
    crew_label = tk.Label(window, text="Select Crew Type:")
    crew_label.grid(row=i+1, column=2, padx=10, pady=10)

    #create available label for each weight entry 
    available_label = tk.Label(window, text="Available Weight:")
    available_label.grid(row=i+1, column=4, padx=10, pady=10)
    #create available output for each weight entry
    available_entry = tk.Entry(window, state="readonly")
    available_entry.grid(row=i+1, column=5, padx=10, pady=10)
    

# create the calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=8, column=1)

# create the result label
result_label = tk.Label(window, text="")
result_label.grid(row=9, column=0, columnspan=2)


window.mainloop()

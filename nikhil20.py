import tkinter as tk

def calculate_total():
    try:
        # Get user input for items and prices
        meal_cost = float(entry_meal.get())
        tax_rate = float(entry_tax.get())
        tip_percent = float(entry_tip.get())

        # Calculate total cost
        tax_amount = meal_cost * (tax_rate / 100)
        tip_amount = meal_cost * (tip_percent / 100)
        total_cost = meal_cost + tax_amount + tip_amount

        # Update the total label
        label_total.config(text=f"Total Cost: ${total_cost:.2f}")
    except ValueError:
        label_total.config(text="Invalid input. Please enter numbers.")

# Create the main window
window = tk.Tk()
window.title("Restaurant Bill Calculator")

# Meal cost entry
label_meal = tk.Label(window, text="Meal Cost:")
label_meal.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
entry_meal = tk.Entry(window)
entry_meal.grid(row=0, column=1, padx=10, pady=10)

# Tax rate entry
label_tax = tk.Label(window, text="Tax Rate (%):")
label_tax.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
entry_tax = tk.Entry(window)
entry_tax.grid(row=1, column=1, padx=10, pady=10)

# Tip percentage entry
label_tip = tk.Label(window, text="Tip Percentage (%):")
label_tip.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
entry_tip = tk.Entry(window)
entry_tip.grid(row=2, column=1, padx=10, pady=10)

# Button to calculate total
button_calculate = tk.Button(window, text="Calculate Total", command=calculate_total)
button_calculate.grid(row=3, column=0, columnspan=2, pady=10)

# Label to display total cost
label_total = tk.Label(window, text="")
label_total.grid(row=4, column=0, columnspan=2, pady=10)

# Run the main loop
window.mainloop()

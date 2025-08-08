import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 == 0:
                result_label.config(text="Error: Division by zero")
                return
            result = num1 / num2
        else:
            result_label.config(text="Select an operation")
            return

        result_label.config(text=f"Result: {result:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Interface set-up
window = tk.Tk()
window.title("Simple Calculator")

# Input numbers
tk.Label(window, text="First Number:").grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(window)
entry1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(window, text="Second Number:").grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(window)
entry2.grid(row=1, column=1, padx=10, pady=5)

# Operation Selection
operation_var = tk.StringVar(value="Add")
operations = ["Add", "Subtract", "Multiply", "Divide"]
tk.Label(window, text="Operation:").grid(row=2, column=0, padx=10, pady=5)
operation_menu = tk.OptionMenu(window, operation_var, *operations)
operation_menu.grid(row=2, column=1, padx=10, pady=5)

# Calcualte button
calc_button = tk.Button(window, text="Calculate", command=calculate)
calc_button.grid(row=3, column=0, columnspan=2, pady=10)

# Results
result_label = tk.Label(window, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Loop again
window.mainloop()

import tkinter as tk

# Initialize the main window
window = tk.Tk()
window.title("Better Calculator")
window.resizable(False, False)

# Variables for display
display_var = tk.StringVar()

# Display Entry (read-only)
display = tk.Entry(window, font=("Arial", 24), borderwidth=2, relief="groove",
                   justify="right", textvariable=display_var, state="readonly")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10, sticky="we")


# Utility functions to update the display
def get_display():
    return display_var.get()

def set_display(value):
    display.config(state="normal")
    display_var.set(value)
    display.config(state="readonly")

# Button functions
def button_click(symbol):
    current = get_display()
    if current == "Error":
        current = ""
    set_display(current + symbol)

def clear_display():
    set_display("")

def backspace():
    current = get_display()
    set_display(current[:-1])

def calculate():
    try:
        expression = get_display().replace("×", "*").replace("÷", "/")
        result = eval(expression)
        set_display(f"{result:.2f}")
    except Exception:
        set_display("Error")

# Keyboard input handler
def key_handler(event):
    key = event.char
    if key in '0123456789.+-*/':
        button_click(key.replace('*', '×').replace('/', '÷'))
    elif key == '\r':  # Enter
        calculate()
    elif key == '\x08':  # Backspace
        backspace()
    elif event.keysym == 'Escape':
        clear_display()

# Bind keyboard keys to the window
window.bind("<Key>", key_handler)

# Calculator button layout
buttons = [
    ['7', '8', '9', '÷'],
    ['4', '5', '6', '×'],
    ['1', '2', '3', '-'],
    ['0', '.', 'C', '+'],
    ['=']
]

# Create and place buttons
for row_idx, row in enumerate(buttons):
    for col_idx, symbol in enumerate(row):
        if symbol == '=':
            btn = tk.Button(window, text=symbol, width=34, height=2, font=("Arial", 16),
                            command=calculate)
            btn.grid(row=row_idx + 1, column=0, columnspan=4, padx=5, pady=5)
        else:
            cmd = clear_display if symbol == 'C' else lambda s=symbol: button_click(s)
            btn = tk.Button(window, text=symbol, width=8, height=2, font=("Arial", 16),
                            command=cmd)
            btn.grid(row=row_idx + 1, column=col_idx, padx=5, pady=5)

# Start the app
window.mainloop()

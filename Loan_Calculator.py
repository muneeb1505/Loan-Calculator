import tkinter as tk
from tkinter import messagebox


def calculate_loan():
    try:
        principal = float(principal_entry.get())
        rate = float(rate_entry.get()) / 100
        time = float(time_entry.get())

        interest = principal * rate * time
        total_payment = principal + interest

        interest_label.config(text=f"Total Interest: ${interest:.2f}")
        total_payment_label.config(text=f"Total Payment: ${total_payment:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")


# Create the main window
root = tk.Tk()
root.title("Loan Calculator")

# Create labels and entries for principal, rate, and time
principal_label = tk.Label(root, text="Loan Amount ($):")
principal_label.grid(row=0, column=0, padx=10, pady=5)
principal_entry = tk.Entry(root)
principal_entry.grid(row=0, column=1, padx=10, pady=5)

rate_label = tk.Label(root, text="Interest Rate (%):")
rate_label.grid(row=1, column=0, padx=10, pady=5)
rate_entry = tk.Entry(root)
rate_entry.grid(row=1, column=1, padx=10, pady=5)

time_label = tk.Label(root, text="Time (years):")
time_label.grid(row=2, column=0, padx=10, pady=5)
time_entry = tk.Entry(root)
time_entry.grid(row=2, column=1, padx=10, pady=5)

# Create button to calculate loan
calculate_button = tk.Button(root, text="Calculate", command=calculate_loan,bg="Blue",fg="White",width="20")
calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="S")

# Create labels to display results
interest_label = tk.Label(root, text="")
interest_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

total_payment_label = tk.Label(root, text="")
total_payment_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Run the main event loop
root.mainloop()

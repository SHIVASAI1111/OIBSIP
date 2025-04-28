
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import csv
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# File to store user data
data_file = 'bmi_data.csv'

# Create data file if it doesn't exist
try:
    with open(data_file, 'x', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "Username", "Weight (kg)", "Height (Meter)", "BMI", "Category"])
except FileExistsError:
    pass

def calculate_bmi():
    try:
        username = name_entry.get().strip()
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if not username:
            raise ValueError("Please enter your name.")

        if weight <= 0 or height <= 0:
            raise ValueError("Please enter valid positive numbers for weight and height.")

        bmi = round(weight / (height ** 2), 2)
        category = classify_bmi(bmi)

        result_label.config(text=f"BMI: {bmi}\nCategory: {category}")

        # Save to file
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(data_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, username, weight, height, bmi, category])

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 24.9 <= bmi < 30.0:
        return "Overweight"
    else:
        return "Obese"

def show_history():
    try:
        username = name_entry.get().strip()
        if not username:
            raise ValueError("Please enter your name to view history.")

        timestamps, bmis = [], []
        with open(data_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["Username"] == username:
                    timestamps.append(row["Timestamp"])
                    bmis.append(float(row["BMI"]))

        if not timestamps:
            raise ValueError("No data found for this user.")

        # Plot
        fig, ax = plt.subplots()
        ax.plot(timestamps, bmis, marker='o')
        ax.set_title(f"BMI History for {username}")
        ax.set_xlabel("Timestamp")
        ax.set_ylabel("BMI")
        ax.tick_params(axis='x', rotation=45)
        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack()

    except ValueError as e:
        messagebox.showerror("History Error", str(e))

# GUI Setup
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("400x500")

# Labels and Inputs
tk.Label(window, text="Name:").pack()
name_entry = tk.Entry(window)
name_entry.pack()

tk.Label(window, text="Weight (kg):").pack()
weight_entry = tk.Entry(window)
weight_entry.pack()

tk.Label(window, text="Height (Meter):").pack()
height_entry = tk.Entry(window)
height_entry.pack()

# Buttons
tk.Button(window, text="Calculate BMI", command=calculate_bmi).pack(pady=10)
result_label = tk.Label(window, text="")
result_label.pack()

tk.Button(window, text="View History", command=show_history).pack(pady=10)

window.mainloop()

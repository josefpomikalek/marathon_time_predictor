"""
This app calculates your likely maximal marathon performance based on your personal best over a shorter course.
"""

from tkinter import *
from ratios import RATIO_10KM, RATIO_HALF_M

window = Tk()
window.title("Marathon Performance Predictor")
window.config(padx=20, pady=20, height=300, width=600, background="moccasin")

# 10 km PB Label
personal_best_10km_label = Label(text="What is you personal best for 10 km run?", background="moccasin", anchor="w")
personal_best_10km_label.grid(row=0, column=0, ipadx=10)

# 10 km PB Entry
personal_best_10km_entry = Entry(width=20)
personal_best_10km_entry.grid(row=0, column=1, padx=20)

# 10 km PB Button
calculate_from_10km_button = Button(text="Calculate max marathon time")
calculate_from_10km_button.grid(row=0, column=2, ipadx=8, ipady=2, padx=20, pady=10)

# Halfmarathon PB Label
personal_best_halfmarathon_label = Label(text="What is your personal best for halfmarathon?", background="moccasin")
personal_best_halfmarathon_label.grid(row=2, column=0)

# Halfmarathon PB Entry
personal_best_halfmarathon_entry = Entry(width=20)
personal_best_halfmarathon_entry.grid(row=2, column=1, padx=10)

# Halfmarathon PB Button
calculate_from_halfmarathon_button = Button(text="Calculate max marathon time")
calculate_from_halfmarathon_button.grid(row=2, column=2, ipadx=8, ipady=2)








window.mainloop()
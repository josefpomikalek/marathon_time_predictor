"""
This app calculates your likely maximal marathon performance based on your personal best over a shorter course.
"""

from tkinter import *
from ratios import RATIO_10KM, RATIO_HALF_M
from math import ceil

window = Tk()
window.title("Marathon Performance Predictor")
window.config(padx=20, pady=20, height=300, width=600, background="moccasin")

# 10 km PB Label
personal_best_10km_label = Label(text="What is your personal best for 10 km run?", background="moccasin",
                                 font=("Arial", 9), anchor="w")
personal_best_10km_label.grid(row=0, column=0, ipadx=10)

# 10 km PB Entry
personal_best_10km_entry = Entry(width=20)
personal_best_10km_entry.grid(row=0, column=1, padx=20)
personal_best_10km_entry.focus()

marathon_time_10km = ""


def pb_10km():

    global marathon_time_10km
    minutes = int(personal_best_10km_entry.get()[:2])
    seconds = int(personal_best_10km_entry.get()[3:])
    time_10km_in_seconds = minutes * 60 + seconds
    marathon_in_seconds = ceil(time_10km_in_seconds * RATIO_10KM)
    print(marathon_in_seconds)
    hours = marathon_in_seconds // 3600
    sec = marathon_in_seconds - (hours * 3600)
    mins = sec // 60
    sec3 = sec - (mins * 60)
    if len(str(mins)) == 1:
        mins = "0" + str(mins)
    print(hours)
    print(sec)
    print(mins)
    print(sec3)
    marathon_time_10km = f"{hours}:{mins}:{sec3}"
    print(marathon_time_10km)
    marathon_time_based_on_10km_label = Label(text=f"Your maximal marathon time based on your 10 km PB is {marathon_time_10km} h.",
                                              background="moccasin", font=("Arial", 12))
    marathon_time_based_on_10km_label.grid(row=3, column=0, columnspan=3, ipady=20, sticky=W)


# 10 km PB Button
calculate_from_10km_button = Button(text="Calculate max marathon time", command=pb_10km)
calculate_from_10km_button.grid(row=0, column=2, ipadx=8, ipady=2, padx=20, pady=10)

# Halfmarathon PB Label
personal_best_halfmarathon_label = Label(text="What is your personal best for halfmarathon?", background="moccasin",
                                         font=("Arial", 9))
personal_best_halfmarathon_label.grid(row=2, column=0)

# Halfmarathon PB Entry
personal_best_halfmarathon_entry = Entry(width=20)
personal_best_halfmarathon_entry.grid(row=2, column=1, padx=10)
personal_best_halfmarathon_entry.insert(0, "h:mm:ss")

# Halfmarathon PB Button
calculate_from_halfmarathon_button = Button(text="Calculate max marathon time")
calculate_from_halfmarathon_button.grid(row=2, column=2, ipadx=8, ipady=2)

# Marathon time Labels

marathon_time_based_on_halfm_label = Label(text="Your maximal marathon time based on your halfmarathon PB is:",
                                           background="moccasin", font=("Arial", 12))
marathon_time_based_on_halfm_label.grid(row=4, column=0, columnspan=3, sticky=W)








window.mainloop()
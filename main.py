"""
This app calculates your likely maximal marathon performance based on your personal best over a shorter course.
You can enter your best 10 km time and/or your best halfmarathon time.
"""

from tkinter import *
from math import ceil

RATIO_10KM = 4.666
RATIO_HALF_M = 2.1

window = Tk()
window.title("Marathon Performance Predictor")
window.geometry("895x240")
window.config(padx=20, pady=20, background="moccasin")

# Information Label
initial_label = Label(text="This app calculates your best marathon time, which you are able to achieve according to your "
                         "PB's for 10 km and/or halfmarathon.", background="moccasin", font=("Arial", 11))
initial_label.grid(row=0, column=0, columnspan=3)

# 10 km PB Label
personal_best_10km_label = Label(text="What is your personal best for 10 km run? Enter your time in format: mm:ss", background="moccasin",
                                 font=("Arial", 10), anchor="w")
personal_best_10km_label.grid(row=1, column=0, ipadx=10)

# Halfmarathon PB Label
personal_best_halfmarathon_label = Label(text="What is your personal best for halfmarathon? Enter your time in format: h:mm:ss", background="moccasin",
                                         font=("Arial", 10))
personal_best_halfmarathon_label.grid(row=2, column=0)

# 10 km PB Entry
personal_best_10km_entry = Entry(width=10)
personal_best_10km_entry.grid(row=1, column=1, padx=20)
personal_best_10km_entry.focus()

# Halfmarathon PB Entry
personal_best_halfmarathon_entry = Entry(width=10)
personal_best_halfmarathon_entry.grid(row=2, column=1, padx=10)

marathon_time_based_on_10km = ""
marathon_time_based_on_halfm = ""


def pb_10km():

    global marathon_time_based_on_10km
    minutes = int(personal_best_10km_entry.get()[:2])
    seconds = int(personal_best_10km_entry.get()[3:])
    time_10km_in_seconds = minutes * 60 + seconds
    marathon_in_seconds = ceil(time_10km_in_seconds * RATIO_10KM)
    hours = marathon_in_seconds // 3600

    sec = marathon_in_seconds - (hours * 3600)
    mins = sec // 60
    secs = sec - (mins * 60)
    if len(str(secs)) == 1:
        secs = "0" + str(secs)
    if len(str(mins)) == 1:
        mins = "0" + str(mins)
    marathon_time_based_on_10km = f"{hours}:{mins}:{secs}"
    print(marathon_time_based_on_10km)
    marathon_time_based_on_10km_label = Label(
        text=f"Your maximal marathon time based on your 10 km PB is {marathon_time_based_on_10km} h.",
        background="moccasin", font=("Arial", 12))
    marathon_time_based_on_10km_label.grid(row=3, column=0, columnspan=3, ipady=20, sticky=W)


def pb_halfm():

    global marathon_time_based_on_halfm
    hours = int(personal_best_halfmarathon_entry.get()[:1])
    minutes = int(personal_best_halfmarathon_entry.get()[2] + personal_best_halfmarathon_entry.get()[3])
    seconds = int(personal_best_halfmarathon_entry.get()[5:])

    time_halfm_in_seconds = hours * 3600 + minutes * 60 + seconds
    marathon_in_seconds = ceil(time_halfm_in_seconds * RATIO_HALF_M)
    hours = marathon_in_seconds // 3600
    sec = marathon_in_seconds - (hours * 3600)
    mins = sec // 60
    secs = sec - (mins * 60)
    if len(str(secs)) == 1:
        secs = "0" + str(secs)
    if len(str(mins)) == 1:
        mins = "0" + str(mins)
    marathon_time_based_on_halfm = f"{hours}:{mins}:{secs}"
    print(marathon_time_based_on_halfm)
    marathon_time_based_on_halfm_label = Label(
        text=f"Your maximal marathon time based on your halfmarathon PB is {marathon_time_based_on_halfm} h.",
        background="moccasin", font=("Arial", 12))
    marathon_time_based_on_halfm_label.grid(row=4, column=0, columnspan=3, sticky=W)


# 10 km PB Button
calculate_from_10km_button = Button(text="Calculate max marathon time", command=pb_10km)
calculate_from_10km_button.grid(row=1, column=2, ipadx=8, ipady=2, padx=20, pady=10)

# Halfmarathon PB Button
calculate_from_halfmarathon_button = Button(text="Calculate max marathon time", command=pb_halfm)
calculate_from_halfmarathon_button.grid(row=2, column=2, ipadx=8, ipady=2)






window.mainloop()
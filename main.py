# Code for a wiki search app, pretty basic|
# ////////////////////////////////////////|
# Welcome to my python wiki searcher app!||
# 1 importing the moduels we need
from tkinter import *    
from wikipedia import *
import pyttsx3
import os
# functions for the proper functioning of search and clear button in line number 67 >>>>

def clear():
    Entry_box.delete(0, END)
    text_box.delete(0.0, END)

# function for the search command/button >>>>>
def search():
    tts.say("wikipedia says.")
    tts.runAndWait()
    data = wikipedia.page(Entry_box.get())
    clear()
    text_box.insert(0.0, data.content)
# read aloud function
def speakit():
    data1 = wikipedia.page(Entry_box.get())
    tts.say(data1.content)
    tts.runAndWait()


# Variable for 'wikipedia says
tts = pyttsx3.init()


# logic and the gui design begins over here >>>
root = Tk()

# setting the title for the window >>>

root.title("WikiSearch it!")

# actually creating a window so you can navigate around >>>

root.geometry("768x700")

# main loop function (this will extend as the code continues and shall not be repeated unless this one is deleted, )
# it is also needed if the code is intented to launch an application window >>>>


# label fram function
_label_ = LabelFrame(root, text="Wiki Search it!")
# configuring the label>>>>

_label_.pack(pady=20)

# adding an entry box and configuring it >>>>>
Entry_box = Entry(_label_, font=("lucida", 18), width=47)
Entry_box.pack(pady=20, padx=20)

# creating and text box frame
text_frame = Frame(root)
text_frame.pack(pady=5)

# create a vertical scroll bar

text_scroll = Scrollbar()
text_scroll.pack(side=RIGHT, fill=Y)


# create a horizontal scroll bar
hor_scroll = Scrollbar(text_frame, orient="horizontal")

# Creating/configuring the text box
text_box = Text(text_frame, yscrollcommand=text_scroll.set, wrap="none", xscrollcommand=hor_scroll.set, font=("lucida"))
text_box.pack()

# configuring the scroll bar go brr >>>>
text_scroll.config(command=text_box.yview)
hor_scroll.config(command=text_box.yview)

# button frame >>>>
button_frame = Frame(root)
button_frame.pack(pady=10)

# creating buttons >>>>
search_button = Button(button_frame, text="Search", font=("lucida", 32), fg="#3a3a3a", command=search)

# configuring buttons >>>>
search_button.grid(row=0, column=1)

# creating the clear screen button and configuring it >>>>
# read aloud button

clear_button = Button(button_frame, text="Clear", font=("lucida", 32), fg="#3a3a3a", command=clear)
clear_button.grid(row=2, column=1)

root.mainloop()



# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 12:35:21 2021

@author: ompra
"""
from tkinter import Label ,Tk
import time

app_windows=Tk()
app_windows.title("DIGITAL CLOCK")
app_windows.geometry("420x150")
app_windows.resizable(1,1)
""" 
Now here I will define the font of the 
time and its colour, its border width 
and the background colour of the digital
 clock

"""
text_font=("Bounder",68,'bold')
background="#f2e750"
foreground="#363529"
border_width= 50
"""
Now here I will combine all the elements
 to define the label of the clock application
 :
"""
label = Label(app_windows, font=text_font, bg=background, fg=foreground, bd=border_width) 
label.grid(row=0, column=1)
"""
Now let’s define the main function of our 

digital clock. Here I will set the text
 of the label as the realtime:

"""
def digital_clock(): 
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live) 
   label.after(200, digital_clock)
   
digital_clock()

app_windows.mainloop()   
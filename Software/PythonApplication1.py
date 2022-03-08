# start by importing all the necessary libraries

from tkinter import *
import tkinter as tk
import pickle
import sys
import time #library to get the current time
from datetime import date
import getpass
import functools
import csv
import pandas as pd
import os.path
pathname = "C:/Users/James/Desktop/Senior Project/PythonApplication1/PythonApplication1/data.csv"
df = None

def displayTime():
    #show the current hour,minute,seconds
  time_now = time.strftime("%H : %M : %S")
    #clock configuration
  clock_label.config(text=time_now)
    #after every 200 microseconds the clock will change
  clock_label.after(200,displayTime)

def dataWind():
    x = Toplevel()
    x.geometry("500x500")

class planner(object):


    def __init__(self, key, data,date, area):
        self.key = key
        self.data = data
        self.date = date
        self.area = area
    
def putdata():  
   global df
   key = what.get()
   data = how.get()
   date = when.get()
   area = where.get()
   df.loc[len(df.index)] = [key,data,date,area]
   print(df.head())
   writefile()

def callremind():
   global remindscreen
   remindscreen = Toplevel(main)
   remindscreen.geometry("300x150")
   remindscreen.grab_set()
   
   global what
   global how
   global when
   global where

   global what_entry
   global how_entry
   global when_entry
   global where_entry
   
   what = StringVar()
   how = StringVar()
   when = StringVar()
   where = StringVar()

   what_label = Label(remindscreen, text='Organization Key').grid(row=0) 
   how_label = Label(remindscreen, text='Reminder data').grid(row=1) 
   when_label = Label(remindscreen, text='Date/Time').grid(row=2) 
   where_label = Label(remindscreen, text='Location').grid(row=3) 

   what_entry = Entry(remindscreen, textvariable= what)
   how_entry = Entry(remindscreen, textvariable= how) 
   when_entry = Entry(remindscreen, textvariable= when)
   where_entry = Entry(remindscreen, textvariable= where)
   what_entry.grid(row=0, column=1) 
   how_entry.grid(row=1, column=1) 
   when_entry.grid(row=2, column=1) 
   where_entry.grid(row=3, column=1) 

   wbtn = Button(remindscreen, text = "ADD", width = 5, height = 1, bg = "blue",fg = "white", command = lambda : putdata())
   wbtn.grid(row = 4, column = 1)

def readFile():
    global df
    file_exists = os.path.exists(pathname)
    if file_exists:
       df = pd.read_csv(pathname)
    else:
        df = pd.DataFrame(columns=['key', 'data', 'date', 'area'])
        print(df.head())
        writefile()

def writefile():
    global df
    if df is None: 
        print("NoneType data frame")
        return
    df.to_csv(pathname, index = False)
    print(df.head())
    
def main_screen():
    global main
    global clock_label
    #Creation of a variable responsible for storing the tkinter window
    main = tk.Tk()
    main.geometry("1000x1000")
    clock_label=Label(main,font=("times",72,"bold"),bg="blue", fg = "white")
    clock_label.grid(row=4,column=0,pady=25,padx=100)
    displayTime()
    digital_clock_title=Label(main,text="Digital Planner",font="times 32 bold", fg ="blue")
    digital_clock_title.grid(row=0,column=0)
    hours_mins_secs=Label(main,text="Hours        Minutes        Seconds",font="times 15 bold", fg = "blue")
    hours_mins_secs.grid(row=5,column=0)
    today  = date.today()
    d2 = today.strftime("%B %d, %Y")
    date_label = Label(main, text = today, font = ("times",54,"bold"), bg = "blue",fg = "white")
    date_label.grid (row=3,column=0)
    reminders  = Label(main, text = "Reminders", font = ("times",32,"bold"), fg = "blue")
    reminders.grid(row = 0, column = 2)
    btn = Button(main, text = "ACCESS DATA", width = 50, height = 5, bg = "blue",fg = "white",  command = dataWind)
    btn.grid(row = 6, column = 0)
    btn2 = Button(main, text = "ACCESS REMINDERS", width = 50, height = 5, bg = "blue",fg = "white", command = callremind)
    btn2.grid(row = 7, column = 0)
    main.mainloop()
    
readFile()
main_screen()

    







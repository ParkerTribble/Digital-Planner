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
RemindArray = []

#Method used to display time on main page
def displayTime():
    #show the current hour,minute,seconds
  time_now = time.strftime("%H : %M : %S")
    #clock configuration
  clock_label.config(text=time_now)
    #after every 200 microseconds the clock will change
  clock_label.after(200,displayTime)
  
#Method used to create window
def dataWind():
    x = Toplevel()
    x.geometry("500x500")

class reminder(object):

    def _init_(memo, priority):
        self.memo = memo
        self.priority = priority

#object creation to hold planner entry data points
class planner(object):


    def __init__(self, key, data,date, area):
        self.key = key #organizational key
        self.data = data #memo about planner entry
        self.date = date #date/due date assoicated with entry
        self.area = area #location assoicated with enrty
    
#retrives input data and call write file to put data in csv file
def putdata():  
   global df
   key = what.get()
   data = how.get()
   date = when.get()
   area = where.get()
   df.loc[len(df.index)] = [key,data,date,area]
   print(df.head())
   writefile()

#creates window for reminder entry
def callremind():
   global remindscreen
   remindscreen = Toplevel(main)
   remindscreen.geometry("300x150")
   remindscreen.grab_set()
   
   global input
   global number
   global input_entry
   sli1 = Scale(remindscreen, from_=1, to=10, tickinterval=1, orient= HORIZONTAL, bg = "blue")
  
   memo = StringVar()
   memo_label = Label(remindscreen, text='MEMO').grid(row=0) 
   memo_entry = Entry(remindscreen, textvariable= memo)
   memo_entry.grid(row=0, column=1) 
   sli1.grid(row = 4, column = 1)
   priority = sli1.get()

   wbtn = Button(remindscreen, text = "ADD", width = 5, height = 1, bg = "blue",fg = "white", command = lambda : putdata())
   wbtn.grid(row = 3, column = 1)
  
def addremind():
    memo = memo.get()

#reads data from csv file/ if no file creates one
def readFile():
    global df
    file_exists = os.path.exists(pathname)
    if file_exists:
       df = pd.read_csv(pathname)
    else:
        df = pd.DataFrame(columns=['key', 'data', 'date', 'area'])
        print(df.head())
        writefile()

#writes data to csv file
def writefile():
    global df
    if df is None: 
        print("NoneType data frame")
        return
    df.to_csv(pathname, index = False)
    print(df.head())
 
#creates popup window for planner entries
def addentry():
   global entryscreen
   entryscreen = Toplevel(main)
   entryscreen.geometry("300x150")
   entryscreen.grab_set()
   
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

   what_label = Label(entryscreen, text='Organization Key').grid(row=0) 
   how_label = Label(entryscreen, text='Reminder data').grid(row=1) 
   when_label = Label(entryscreen, text='Date/Time').grid(row=2) 
   where_label = Label(entryscreen, text='Location').grid(row=3) 

   what_entry = Entry(entryscreen, textvariable= what)
   how_entry = Entry(entryscreen, textvariable= how) 
   when_entry = Entry(entryscreen, textvariable= when)
   where_entry = Entry(entryscreen, textvariable= where)
   what_entry.grid(row=0, column=1) 
   how_entry.grid(row=1, column=1) 
   when_entry.grid(row=2, column=1) 
   where_entry.grid(row=3, column=1) 

   wbtn = Button(entryscreen, text = "ADD", width = 5, height = 1, bg = "blue",fg = "white", command = lambda : putdata())
   wbtn.grid(row = 4, column = 1)

#Main window method, contains "mainloop"
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
    btn = Button(main, text = "ACCESS PLANNER DATA", width = 50, height = 5, bg = "blue",fg = "white",  command = dataWind)
    btn.grid(row = 6, column = 0)
    btn2 = Button(main, text = "ADD REMINDER", width = 50, height = 5, bg = "blue",fg = "white", command = callremind)
    btn2.grid(row = 8, column = 0)
    btn3 = Button(main, text = "ADD PLANNER ENTRY", width = 50, height = 5, bg = "blue", fg = "white", command = addentry)
    btn3.grid(row = 7, column = 0)
    main.mainloop()
    
readFile()
main_screen()


    







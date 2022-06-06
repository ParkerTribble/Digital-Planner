################################################
#### Mobile Unit Code for Senior Project #######
###### Parker Tribble Elizabehtown College #####
############# 4 - 8 - 2022 #####################
################################################
# start by importing all the necessary libraries

from tkinter import * #tkinter GUI library
import tkinter as tk #importing as obj
import sys
import time #library to get the current time
from datetime import date #gets current time and date from device
import getpass
import functools
import csv #import library to work with csv files
import pandas as pd #pandas library for dataframe use
import os.path #allows for reading and writing pathways 
pathname = "/home/tribble/Desktop/df/data.csv" #locations of csv holding planner entries
pathname2 = "/home/tribble/Desktop/df/reminder.csv" #location of csv files holding reminders
df = None #df for planner entires 
df2 = None #df for reminder entries 

##############################################
# PROCESS DATA TO AND FROM CSV FILES
##############################################

#reads data from csv file/ if not file creates one
def readFile():
    global df
    file_exists = os.path.exists(pathname)
    if file_exists:
       df = pd.read_csv(pathname)
    else:
        df = pd.DataFrame(columns=['key', 'data', 'date', 'area'])
        writefileData()
    global df2
    file_exists2 = os.path.exists(pathname2)
    if file_exists2:
       df2 = pd.read_csv(pathname2)
    else:
        df2 = pd.DataFrame(columns=['Priority', 'Memo'])
        writefileRemind()

#writes planner entires to csv file
def writefileData():
    global df
    if df is None: 
        print("NoneType data frame")
        return
    df.to_csv(pathname, index = False)
    #print(df.head())
    None

#writes reminders to csv file 
def writefileRemind():
    global df2
    if df2 is None: 
        print("NoneType data frame")
        return
    df2.to_csv(pathname2, index = False)
    #print(df.head())
    None

##############################################
# HANDILING DATA FOR PLANNER
##############################################

 #object creation to hold planner entry data points
class planner(object):


    def __init__(self, key, data,date, area):
        self.key = key #organizational key
        self.data = data #memo about planner entry
        self.date = date #date/due date assoicated with entry
        self.area = area #location assoicated with enrty
        None

#retrives input data and call write file to put data in csv filW for planner entries
def putdata():  
   global df
   key = what.get()
   data = how.get()
   date = when.get()
   area = where.get()
   df.loc[len(df.index)] = [key,data,date,area]
   print(df.head())
   writefileData()

#creates popup window for planner entries
def addentry():
   global entryscreen
   entryscreen = Toplevel(main)
   entryscreen.geometry("500x200")
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

##############################################
# HANDILING DATA FOR REMINDER
##############################################

#object to hold reminder entry data
class reminder(object):

    def _init_(self, memo, priority):
        self.memo = memo
        self.priority = priority

##retrives input data and call write file to put data in csv file for reminder entries
def addremind():
    readFile()
    df2.fillna('')
    list = df2.values.flatten()
    #print("list", list)
    check = input.get()
    print("MEMO",check)
    if(check != ''):
        memo = check
        priority = number.get()
        df2.loc[len(df2.index)] = [priority,memo]
        print(df2.head)
        writefileRemind()
#used in rmremind to adjust the data frame data
def adjdf(filler):
    print('filler in adj function')
    print(filler)
    df2 = filler
    df2.to_csv(pathname2, index = False)
    print('df2')
    print(df2)
#removes selected reminders from CSV file
def rmremind(Varlist):
  counter = 1
  tracker= 0
  filler = df2
  print('filler before drop')
  print(df2)
  for x in Varlist:
      if Varlist[tracker] == 1 :
         filler =  df2.drop([tracker])
         print('filler after drop')
         print(filler)
         adjdf(filler)
      counter += 1
      tracker += 1

 ##############################################
# DISPLAY WINDOWS AND FUNCTIONS USED
##############################################

#compares current string to a list of strings. returns list of zeros. if theres a 1 in the list it means var matched character in list
def compare(var,list):
   # print('Compare called')
   # print(var)
   # print(list)
    int = 0
    templist = [0]*10
    while int < len(list):
        if var == list[int]:
            templist[int] = 1
           # print('templist adjusted')
        else:
           # print('no change made')
           None
        int += 1
   # print('returning compared value')
    return templist

#scans csv file for unique keys, IS CASE SENSITIVE, utilizses compare function
def getkeylist():
    keys = df['key']
    #print(keys)
    key_list = [keys[0]]
    print(key_list)
    comparelist = [0]*10
    for x in keys:
        #print('current key:')
        #print(x)
        if x == key_list[0]:
            #print('matches so skip')
            None
        else:
        # print('doesnt match, calling comapre')
            checklist = compare(x,key_list)
     #   print('checking compared')
            if checklist == comparelist:
        #   print('adding new key to key_list')
                if x != 'nan':
                    key_list.append(x)
            else:
        #    print('No change needed')
             None
    print('\n\n\n list of all keys:')
    print(key_list)
    key_list = [str(x) for x in key_list]
    newlist = [x for x in key_list if x != 'nan']
    print(newlist)
    return key_list


 ##############################################
# MAIN WINDOW AND FUNCTIONS
##############################################

  #Main window method, contains "mainloop"
def main_screen():
    global main
    global clock_label
    #Creation of a variable responsible for storing the tkinter window
    main = tk.Tk()
    main.geometry("700x1000")
    main.configure(bg = "#5b5b5b")
    #frame = Frame(main)
    #frame.pack()
    clock_label=Label(main,font=("times",20), fg = "#fff5e5", bg = "#5b5b5b")
    clock_label.grid(row = 1, column = 1)
    displayTime()
    digital_clock_title=Label(main,text="Mobile Unit",font=("times 25 underline"), fg ="#fff5e5", bg = "#5b5b5b")
    digital_clock_title.grid(row = 0, column = 0)
    hours_mins_secs=Label(main,text="Add Planner Entries",font="times 16 italic bold", fg = "#fff5e5",  bg = "#5b5b5b")
    hours_mins_secs.grid(row=1,column=0)
    today  = date.today()
    d2 = today.strftime("%B %d, %Y")
    date_label = Label(main, text = today, font = ("times",20),fg= "#fff5e5", bg = "#5b5b5b")
    date_label.grid(row=0,column=1)
    #reminders  = Label(main, text = "Reminders", font = ("times",32,"bold"), fg = "blue")
    #reminders.grid(row = 0, column = 2)
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

    what_label = Label(main, text='Organization Key', bg = "#5b5b5b", fg = "#fff5e5").grid(row=3, column = 0) 
    how_label = Label(main, text='Reminder data', bg = "#5b5b5b", fg = "#fff5e5").grid(row=3, column = 1) 
    when_label = Label(main, text='Date/Time', bg = "#5b5b5b", fg = "#fff5e5").grid(row=5, column = 0) 
    where_label = Label(main, text='Location', bg = "#5b5b5b", fg = "#fff5e5").grid(row=5, column = 1) 

    what_entry = Entry(main, textvariable= what)
    how_entry = Entry(main, textvariable= how) 
    when_entry = Entry(main, textvariable= when)
    where_entry = Entry(main, textvariable= where)
    what_entry.grid(row=4, column=0) 
    how_entry.grid(row=4, column=1) 
    when_entry.grid(row=6, column=0) 
    where_entry.grid(row=6, column=1) 

    wbtn = Label(main, text = "REMINDERS", width = 15, height = 1, bg = "#fff5e5")
    wbtn.grid(row = 0, column = 3)
    wbtn2 = Button(main, text = "ADD", width = 15, height = 1, bg = "#fff5e5", fg = "#5b5b5b", command = lambda : putdata())
    wbtn2.grid(row = 7, column = 0)

  
    #remind_label = Label(main, text = 'Reminders', font=("times",25,"underline"), bg = "#5b5b5b", fg = "#fff5e5").grid(row = 0, column = 2)
    #instructions = Label(main, text = 'Check the box \n Then click delete to remove', font=("times",12,"italic bold"), bg = "#5b5b5b", fg = "#fff5e5").grid(row = 1, column = 2)
    #instructions2 = Label(main, text = 'Then click complete to remove', font=("times",12), bg = "#5b5b5b", fg = "#fff5e5").grid(row = 2, column = 2)
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    var6 = IntVar()
    var7 = IntVar()
    var8 = IntVar()
    var9 = IntVar()
    var10 = IntVar()
    text0 = df2.iloc[0][1]
    text1 = df2.iloc[1][1]
    text2 = df2.iloc[2][1]
    text3 = df2.iloc[3][1]
    text4 = df2.iloc[4][1]
    text5 = df2.iloc[5][1]
    text6 = df2.iloc[6][1]
    text7 = df2.iloc[7][1]
    text8 = df2.iloc[8][1]
    text9 = df2.iloc[9][1]
    chkbtn = Checkbutton(main, text = text0, variable = var1, onvalue = 1, offvalue = 0, bg = "#5b5b5b", fg = "#fff5e5")
    chkbtn.grid(row = 1, column = 3)
    chkbtn1 = Checkbutton(main, text = text1, variable = var2, onvalue = 1, offvalue = 0, bg = "#5b5b5b", fg = "#fff5e5")
    chkbtn1.grid(row = 2, column = 3)
    chkbtn2 = Checkbutton(main, text = text2, variable = var3, onvalue = 1, offvalue = 0, bg = "#5b5b5b", fg = "#fff5e5")
    chkbtn2.grid(row = 3, column = 3)
    chkbtn3 = Checkbutton(main, text = text3, variable = var4, onvalue = 1, offvalue = 0, bg = "#5b5b5b", fg = "#fff5e5")
    chkbtn3.grid(row = 4, column = 3)
    chkbtn4 = Checkbutton(main, text = text4, variable = var5, onvalue = 1, offvalue = 0, bg = "#5b5b5b", fg = "#fff5e5")
    chkbtn4.grid(row = 5, column = 3)
    chkbtn5 = Checkbutton(main, text = text5, variable = var6, onvalue = 1, offvalue = 0, bg = "#5b5b5b", fg = "#fff5e5")
    chkbtn5.grid(row = 6, column = 3)
    chkbtn6 = Checkbutton(main, text = text6, variable = var7, onvalue = 1, offvalue = 0, bg = "#5b5b5b", fg = "#fff5e5")
    chkbtn6.grid(row = 7, column = 3)
    chkbtn7 = Checkbutton(main, text = text7, variable = var8, onvalue = 1, offvalue = 0, bg = "#5b5b5b", fg = "#fff5e5")
    chkbtn7.grid(row = 8, column = 3)
    chkbtn8 = Checkbutton(main, text = text8, variable = var9, onvalue = 1, offvalue = 0, bg = "#5b5b5b", fg = "#fff5e5")
    chkbtn8.grid(row = 9, column = 3)
    chkbtn9 = Checkbutton(main, text = text9, variable = var10, onvalue = 1, offvalue = 0, bg = "#5b5b5b", fg = "#fff5e5")
    chkbtn9.grid(row = 10, column = 3)
    


    main.mainloop()

#Method used to display time on main page
def displayTime():
    #show the current hour,minute,seconds
  time_now = time.strftime("%H : %M : %S")
    #clock configuration
  clock_label.config(text=time_now)
    #after every 200 microseconds the clock will change
  clock_label.after(200,displayTime)


##############################################
# MAIN CODE
##############################################

readFile()
main_screen()
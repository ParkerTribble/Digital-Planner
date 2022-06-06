
################################################
###### Terminal Code for Senior Project ########
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
destination = '/home/tribble/Desktop/data_mobile.csv' #location of data file on mobile unit
destination2 = "/home/tribble/Desktop/reminder_mobile.csv" #location of reminder file on mobile unit
df = None #df for planner entires 
df2 = None #df for reminder entries 
tempdf = None
combinedf = None
import pysftp
import pysftp as sftp


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

def sftpdata():
    host = '10.0.0.196'
    username = 'tribble'
    password = 'klpp64'
    conn = pysftp.Connection(host= '10.0.0.196',port=22,username= 'tribble', password='klpp64')
    print("connection established successfully")
    conn.put(pathname2,destination2)
    conn.get(destination,'/home/tribble/Desktop/df/temp.csv')
    global tempdf
    global df
    tempdf = pd.read_csv('/home/tribble/Desktop/df/temp.csv')
    df = df.append(tempdf, ignore_index = True)
    print(df)
    print('\n\n')
    df = df.drop_duplicates()
    df.sort_values(["key","data"], inplace = True)
    print(df)
    
   
    

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

#retrives input data and call write file to put data in csv file for planner entries
def putdata():  
   global df
   key = what.get()
   data = how.get()
   date = when.get()
   area = where.get()
   df.loc[len(df.index)] = [key,data,date,area]
   print(df.head())
   writefileData()
   what_entry.delete(0,'end')
   how_entry.delete(0,'end')
   when_entry.delete(0,'end')
   where_entry.delete(0,'end')

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

   list = getkeylist()
   key_label = Label(entryscreen, text = 'Current Keys:').grid(row=0,column=3)
   j = 1
   for x in list:
        filler_label = Label(entryscreen, text = '    ').grid(row=j,column=2)
        loop_label = Label(entryscreen, text = x).grid(row=j,column=3)
        j+=1

def removeentry(num):
   filler = df
   filler = df.drop([num])
   filler.to_csv(pathname, index = False)
   readFile()

def rmplanner():
   global rmscreen
   rmscreen = Toplevel(main)
   rmscreen.geometry("500x500")
   rmscreen.grab_set()
   frame = Frame(rmscreen)
   frame.pack()
   number = IntVar()
   labellabel = Label(rmscreen, text = "REMOVE PLANNER ENTIRES", font = "times 24 bold", bg = 'blue', fg = 'white').pack(side = TOP)
   labeltest = Label(rmscreen, text= df, font=('times',12)).pack(side = TOP)
   number_label = Label(rmscreen, text = "Please enter row number of entry to be deleted", font = "times 12 bold", fg = 'blue').pack(side = TOP)
   number_entry = Entry(rmscreen, textvariable= number).pack(side = TOP)
   btn = Button(rmscreen, text = "Delete", font = "times 12 bold", fg = 'white', bg= 'blue', command = lambda: removeentry(number.get())).pack(side = TOP) 

def organizedata():
    df.sort_values("key", inplace = True)
    writefileData()


##############################################
# HANDILING DATA FOR REMINDER
##############################################

#object to hold reminder entry data
class reminder(object):

    def _init_(self, memo, priority):
        self.memo = memo
        self.priority = priority

#creates window for reminder entry
def callremind():
   global remindscreen
   remindscreen = Toplevel(main)
   remindscreen.geometry("500x200")
   remindscreen.grab_set()
   #frame1 = Frame(remindscreen)
   #frame1.pack()
   list = df2.size
   #if(list > 20):
   global input
   global number
   global input_entry
   global number_entry
   sli1 = Scale(remindscreen, from_=1, to=10,length = 200 ,tickinterval=1, orient= HORIZONTAL, bg = "blue", fg = 'white', font = ("times", 10, "bold"))
   input = StringVar()
   input_label = Label(remindscreen, text='ADD NEW REMINDERS', bg = 'blue', fg = 'white',font=("times",24,"bold") ).grid( row = 0, column = 2)
   input_entry = Entry(remindscreen, textvariable= input, width = 50)
   textlabel = Label(remindscreen, text= 'enter text:', fg = 'blue', font = ("times",10,"bold")).grid(row =1 , column = 1)
   input_entry.grid( row = 1, column = 2)
   sli1.grid( row = 2, column = 2)
   number = sli1
   wbtn = Button(remindscreen, text = "ADD", width = 5, height = 1, bg = "blue",fg = "white", font = ("times", 16,"bold") ,command = lambda : addremind())
   wbtn.grid( row =3, column = 2)

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
    input_entry.delete(0,'end')

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
    return newlist

#Method used to create window displaying planner data
def dataWind():
    global plandisplay
    plandisplay = Toplevel()
    plandisplay.geometry("750x400")
    plandisplay.grab_set()
    #planframe = Frame(plandisplay)
    #planframe.pack( side = TOP )
    keys = getkeylist()
    track = 0 
    for p in keys:
        testlabel = Label(plandisplay, text = p, font=("times",24,"bold"),bg="blue", fg = "white").grid(row = 0, column = track)
        blanklabel = Label(plandisplay, text = '   ').grid(row = 0, column = track+1)
        track+=2
    keytrack = 0
    for y in keys:
        print(keytrack)
        rowtrack = 1
        dftrack = 0
        for x in df['key']:
            #print(rowtrack)
            #print(x + y)
            if x == y:
                 print('Matching, adding filler')
                 data = df.iloc[dftrack][1] +' '+ df.iloc[dftrack][2] +' '+ df.iloc[dftrack][3]
                 testlabel = Label(plandisplay, text = data, font=("times",12,"bold"), fg = "black").grid(row = rowtrack, column = keytrack)
                 rowtrack += 1
            print(dftrack)
            dftrack+=1
        keytrack+=2
    
 #Method used to create window displaying reminder data
def displayremind():
    global remindscreen
    remindscreen = Toplevel(main)
    remindscreen.geometry("350x500")
    remindscreen.grab_set()
    remindframe = Frame(remindscreen)
    remindframe.pack( side = TOP )
    remind_label = Label(remindscreen, text = 'Reminders', font=("times",48,"bold"),bg="blue", fg = "white").pack( side = TOP )
    instructions = Label(remindscreen, text = 'After completing a reminder check the box', font=("times",12,"bold"),fg = "blue").pack( side = TOP )
    instructions2 = Label(remindscreen, text = 'click complete button to remove once checked', font=("times",12,"bold"),fg = "blue").pack( side = TOP )
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
    chkbtn = Checkbutton(remindscreen, text = text0, variable = var1, onvalue = 1, offvalue = 0)
    chkbtn.pack( side = TOP )
    chkbtn1 = Checkbutton(remindscreen, text = text1, variable = var2, onvalue = 1, offvalue = 0)
    chkbtn1.pack( side = TOP )
    chkbtn2 = Checkbutton(remindscreen, text = text2, variable = var3, onvalue = 1, offvalue = 0)
    chkbtn2.pack( side = TOP )
    chkbtn3 = Checkbutton(remindscreen, text = text3, variable = var4, onvalue = 1, offvalue = 0)
    chkbtn3.pack( side = TOP )
    chkbtn4 = Checkbutton(remindscreen, text = text4, variable = var5, onvalue = 1, offvalue = 0)
    chkbtn4.pack( side = TOP )
    chkbtn5 = Checkbutton(remindscreen, text = text5, variable = var6, onvalue = 1, offvalue = 0)
    chkbtn5.pack( side = TOP )
    chkbtn6 = Checkbutton(remindscreen, text = text6, variable = var7, onvalue = 1, offvalue = 0)
    chkbtn6.pack( side = TOP )
    chkbtn7 = Checkbutton(remindscreen, text = text7, variable = var8, onvalue = 1, offvalue = 0)
    chkbtn7.pack( side = TOP )
    chkbtn8 = Checkbutton(remindscreen, text = text8, variable = var9, onvalue = 1, offvalue = 0)
    chkbtn8.pack( side = TOP )
    chkbtn9 = Checkbutton(remindscreen, text = text9, variable = var10, onvalue = 1, offvalue = 0)
    chkbtn9.pack( side = TOP )
    but = Button(remindscreen, text = 'Complete', fg = 'white', bg = 'blue', command = lambda: rmremind(Varlist = [var1.get(),var2.get(),var3.get(),var4.get(),var5.get(),var6.get(),var7.get(),var8.get(),var9.get(),var10.get()])).pack( side = TOP )

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
    clock_label=Label(main,font=("times",72,"bold"),bg="blue", fg = "white")
    clock_label.grid(row=2,column=0,pady=25,padx=100)
    displayTime()
    digital_clock_title=Label(main,text="Digital Planner",font="times 32 bold", fg ="blue")
    digital_clock_title.grid(row=0,column=0)
    hours_mins_secs=Label(main,text="Hours        Minutes        Seconds",font="times 15 bold", fg = "blue")
    hours_mins_secs.grid(row=3,column=0)
    today  = date.today()
    d2 = today.strftime("%B %d, %Y")
    date_label = Label(main, text = today, font = ("times",54,"bold"), bg = "blue",fg = "white")
    date_label.grid (row=1,column=0)
    #reminders  = Label(main, text = "Reminders", font = ("times",32,"bold"), fg = "blue")
    #reminders.grid(row = 0, column = 2)
    btn = Button(main, text = "ACCESS PLANNER DATA", width = 50, height = 2, bg = "blue",fg = "white",  command = dataWind)
    btn.grid(row = 4, column = 0)
    btn2 = Button(main, text = "ADD REMINDER", width = 50, height = 2, bg = "blue",fg = "white", command = callremind)
    btn2.grid(row = 8, column = 0)
    btn3 = Button(main, text = "ADD PLANNER ENTRY", width = 50, height = 2, bg = "blue", fg = "white", command = addentry)
    btn3.grid(row = 5, column = 0)
    btn4 = Button(main, text = "OPEN REMINDERS", width = 50, height = 2, bg = "blue", fg = "white", command = displayremind)
    btn4.grid(row = 7, column = 0)
    btn5 = Button(main, text = 'EDIT PLANNER DATA', width = 50, height = 2, bg = "blue",fg = "white", command = rmplanner)
    btn5.grid(row = 6, column = 0)
    btn6 = Button(main, text = "COLLECT DATA", width = 50, height = 2, bg = "blue", fg = "White", command = sftpdata)
    btn6.grid(row = 9, column = 0)
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
organizedata()
main_screen()




            
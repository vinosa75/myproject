
# Python program to create a table
   
from tkinter import *

import tkinter as tk

from functools import partial 


def call_result(label_result, n1, n2):  
    num1 = (n1.get())  
    num2 = (n2.get())  
    result = int(num1)+int(num2)  
    label_result.config(text="Result = %d" % result)  
    return


    
class Table:
      
    def __init__(self,root):

                # create a horizontal scrollbar by
        # setting orient to horizontal
          
        # code for creating table
        for i in range(4,total_rows):
            for j in range(total_columns):
                  
                self.e = Entry(root, width=50, fg='black',
                               font=('Arial',10,'bold'))
                  
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])
  

EntryPrice = 15135
StrikePrice	= 14950

outputValue = (EntryPrice-StrikePrice)/4
count = 0

lst = []

for i in range(0,10):
    
    print(outputValue)
    NewValue = outputValue*(i+1)

    OneFourth = round(outputValue*(count+0.25),2)
    Half = round(outputValue*(count+0.50),2)
    ThreeFourth = round(outputValue*(count+0.75),2)

    count = count+1

    
    lst.append((str(i)+"(3\\4)",ThreeFourth))
    lst.append((str(i)+"(1\\5)",Half))
    lst.append((str(i)+"(1\\4)",OneFourth))
    lst.append((i,NewValue))


# lst.append(("S.no","Value",'1\\4','1\\2','3\\4'))

def Reverse(lst):
    return [ele for ele in reversed(lst)]
      
# Driver Code
lst = Reverse(lst)

# reversed(lst)


# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])
   
# create root window
root = Tk()
t = Table(root)

 
    
t.grid(row=7, column=2)  

number1 = tk.StringVar()  
number2 = tk.StringVar()

labelNum1 = tk.Label(root, text="A").grid(row=1, column=0)  
    
labelNum2 = tk.Label(root, text="B").grid(row=2, column=0) 

entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)  
    
entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2) 


call_result = partial(call_result, t, number1, number2)  
    
buttonCal = tk.Button(root, text="Calculate").grid(row=3, column=0) 


# call_result = partial(call_result, labelResult, number1, number2)  

root.mainloop()
import requests
import csv
import random
import json
import sys
import tkinter as tk

def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    for repo in new_data:
        temp=repo["total_issues"]
        for i in range(temp):
            if(repo["issues"][i]==inp):
                lbl.config(text = "Repo id: "+str(repo["id"])+" and name:"+repo["name"])

  
r = requests.get("https://dev-api.metabob.com/repositories/?current_page=0&page_size=25")
old_data = r.json()
    
new_data=old_data

with open('errors.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

errors=data[0]

for repo in new_data:
    temp=random.randint(0,3)
    repo["total_issues"]=temp
    for i in range(temp):
        temp=random.randint(0,29)
        repo["issues"].append(errors[temp])


        
frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('400x200')

  

inputtxt = tk.Text(frame,
                   height = 5,
                   width = 20)
  
inputtxt.pack()
  

printButton = tk.Button(frame,
                        text = "Print", 
                        command = printInput)
printButton.pack()
  

lbl = tk.Label(frame, text = "")
lbl.pack()
frame.mainloop()





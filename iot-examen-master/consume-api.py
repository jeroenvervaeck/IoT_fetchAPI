import json
import requests
import tkinter
from tkinter import *


def saveFile(username):
    with open('users.txt', 'a+') as file:
        # a+ = append + create file if doesn't exist
        file.write('username: ' + username + "\n")
    
    

try:
    response = requests.get('https://uinames.com/api/').json()
    print('Saving file')
    username = response['name']
    saveFile(username)
except Exception as e:
    print('Bad response from the server: ' + str(e))


root = Tk()

var = StringVar()
label = Label( root, textvariable = var, relief = RAISED )
button = Button(root, text="OK", command=root.destroy)

var.set(username)
label.pack()
button.pack()
root.mainloop()
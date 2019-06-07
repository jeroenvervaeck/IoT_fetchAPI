import tkinter as tk
import requests
from pprint import pprint
import json


HEIGHT = 500
WIDTH = 600
def response_format(json_data):
	#get the information you want from the json data
	try:
		name = json_data['results'][0]['name']['first'];
		gender = json_data['results'][0]['name']['last'];
		location = json_data['results'][0]['location']['city'];	
		output =  'Firstname: %s \nLastname: %s \nLocation: %s' % (name, gender, location)
	except:
		output = 'There wa a problem retrieving that information'
	return output
def search(entry):
	# fetch API and shown a user profile base on the enrty that is given (male or female)
	url = "https://randomuser.me/api/"
	param = {'gender': entry}
	json_data = requests.get(url,params=param).json()
	#pprint(json_data)
	#write output into the lower frame label
	message['text'] = response_format(json_data)
	#append the new json data to data.json
	with open ('users.json','a') as f:
		collected_data = json.dump(json_data, f);
		repr(collected_data);
	

root = tk.Tk()

#Creating our 'canvas' window
canvas = tk.Canvas(root, width = WIDTH, height= HEIGHT)
canvas.pack()
#end canvas window

#Background image	
background_image = tk.PhotoImage(file='background.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relheight=1, relwidth=1)
#end background image

#top frame (blue thingy)
frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1 ,anchor='n')

entry = tk.Entry(frame, text="type in gender")
entry.place(relwidth=0.75, relheight=1)

button = tk.Button(frame, text='Search', command=lambda: search(entry.get()))
button.place(relx =0.80, relwidth=0.2, relheight=1)
#end top frame

#bottom frame
frame_bottom = tk.Frame(root, bg='#80c1ff', bd=5)
frame_bottom.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.65 ,anchor='n')

#Box to show output from API
message = tk.Label(frame_bottom, bg='white', font=('Courier', 18))
message.place(relwidth=1, relheight= 1)

#end of bottom frame
root.mainloop()

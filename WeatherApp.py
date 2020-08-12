import tkinter as tk
from tkinter import font
import requests




HEIGHT = 600
WIDTH  = 900


# pro.openweathermap.org/data/2.5/forecast/hourly?q={city name}&appid={your api key}

def format_response(weather):
	try: 
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']
		feels = weather['main']['feels_like']

		final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s \nPork says it feels like: %s \n' % (name,desc,temp,feels)
	except:
		final_str = 'Porkchop couldnt find any info on this location'

	return final_str

def get_weather(city):
	weather_key ='edffd1bf975a74d5d10e58c5ac8be2d3'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params ={ 'APPID': weather_key, 'q': city, 'units':'imperial'}
	response = requests.get(url, params = params)
	weather = response.json()
	print(response.json())

	label['text'] = format_response(weather)

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='weatherlandscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#296D98', bd=5)
frame.place(relx=.5, rely=.1, relwidth=0.75, relheight=0.1, anchor='n')

button = tk.Button(frame, text="Ask Porkchop", font=('Courier',12), command=lambda: get_weather(entry.get()))
button.place(relx=.7, relwidth=.3, relheight=1)

entry = tk.Entry(frame, font=40)
entry.place(relwidth=.65, relheight=1)

lower_frame = tk.Frame(root, bg='#92CDCD', bd=5)
lower_frame.place(relx=.5, rely=.25, relwidth=.75, relheight=.4, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 18), bd=4)
label.place(relwidth=1, relheight=1)

# Find fonts available
# print(tk.font.families())

root.mainloop()
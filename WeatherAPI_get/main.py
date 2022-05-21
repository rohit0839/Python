from cgitb import text
from turtle import home
import tkinter as tk
import requests
import json
lon,lat = str(77.102493), str(12.971599) # Bangalore

# https://www.7timer.info/doc.php?lang=en#api
response = requests.get("http://www.7timer.info/bin/api.pl?lon="+lon+"&lat="+lat+"&product=civillight&output=json")
#print(response.status_code)

data = response.json()
#print(data)
#with open('data.json', 'w') as f:
#    json.dump(data, f)

for x in range(7):
    max_t = data['dataseries'][x]['temp2m']['max']
    min_t = data['dataseries'][x]['temp2m']['min']
    print(f'{x+1}# max : {max_t} min : {min_t}',sep='\n')

window = tk.Tk()
window.title("Weather App")
window.geometry("700x350")
max_t1 = data['dataseries'][0]['temp2m']['max']
min_t1 = data['dataseries'][0]['temp2m']['min']
max_t2 = data['dataseries'][1]['temp2m']['max']
min_t2 = data['dataseries'][1]['temp2m']['min']
B1 = tk.Button(text =f'Today     # max : {max_t1}, min : {min_t1}',)
B1.pack()
B2 = tk.Button(text =f'Tommorrow # max : {max_t2}, min : {min_t2}',)
B2.pack()
window.mainloop()
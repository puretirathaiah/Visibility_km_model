The aim is to implement a model to predict the visibility given the weather conditions.

Data: Webscrapped the climate data from the website: https://en.tutiempo.net/ for Luxembourg for the years 2010 to 2020.

Note: Data has been missed for a certain days in every month.

Abbreviations:

T	Average Temperature (°C)
TM	Maximum temperature (°C)
Tm	Minimum temperature (°C)
SLP	Atmospheric pressure at sea level (hPa)
H	Average relative humidity (%)
PP	Total rainfall and / or snowmelt (mm)
VV	Average visibility (Km)
V	Average wind speed (Km/h)
VM	Maximum sustained wind speed (Km/h)
VG	Maximum speed of wind (Km/h)
RA	Indicate if there was rain or drizzle (In the monthly average, total days it rained)
SN	Snow indicator (In the monthly average, total days that snowed)
TS	Indicates whether there storm (In the monthly average, Total days with thunderstorm)
FG	Indicates whether there was fog (In the monthly average, Total days with fog)

Visibility.ipynb: The Jupytor notebook file is used to explore different models to find an optimal model for the problem.

visibility_model.py: The python file contains an optimal model for the problem.

To deploy the model:
	- download all the folders
	- run the visibility_model.py if the model want to be saved to folder (if visibility_model.pkl is not present in the folder) 
	- Go to the file location in cmd
		>>> set FLASK_APP=app.py
		>>> flask run
	- Use the url http://127.0.0.1:5000/ in a browser window, where we can give inputs to predict the visibility 

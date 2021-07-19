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

Visibility.ipynb: This Jupytor notebook file is used to explore different models to find the optimal model for this problem.

visibility_model.py: It contains the optimal model for this problem.

To deploy the model:

	Go to the file location in cmd:

	>>> set FLASK_APP=app.py
	>>> flask run
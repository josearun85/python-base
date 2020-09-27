# Build an API server
# Flask to build an API
from flask import Flask, request
import json
# geocoding imports
from geopy.geocoders import Nominatim
import time
from pprint import pprint
import pandas as pd
import geopandas
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

app=Flask(__name__)
app_geo = Nominatim(user_agent="tutorial")


	 
def createPlot(df):

	gdf = geopandas.GeoDataFrame(
		df, geometry=geopandas.points_from_xy(df.lon, df.lat))
		
	world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))

	# We restrict to South America.
	ax = world.plot(
		color='white', edgecolor='black')

	# We can now plot our ``GeoDataFrame``.
	gdf.plot(ax=ax, color='red')

	plt.savefig("map.png")

@app.route("/geocode",methods=["POST"])	
def getlatlon():
	print("Received request:",request.json)
	
	location = app_geo.geocode(request.json["query"]).raw
	print(location)
	df_tmp = pd.DataFrame(
    {'city': [request.json["query"]],
     'country': [location["display_name"].split(", ")[-1]],
     'lat': [float(location["lat"])],
     'lon': [float(location["lon"])]})

	print(df_tmp)
	createPlot(df_tmp)
	return json.dumps({"location":location}),200
	
	
print("This is my server")

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5001)
	

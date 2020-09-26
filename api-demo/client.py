# Client code
import requests
import json

print("this is my client")
import pandas as pd
import geopandas
import matplotlib.pyplot as plt


df = pd.DataFrame(
    {'city': ["Bangalore","New York"],
     'country': ["",""],
     'lat': [0,0],
     'lon': [0,0]})

url = "http://localhost:5000/geocode"

for i in range(0,df.shape[0]):
	body = {"query" : df.loc[i,'city']}
	print(body)
	my_req = requests.post(url, json=body)
	response = json.loads(my_req.content)
	print(response)
	df.loc[i,"lat"] = response["location"]["lat"]
	df.loc[i,"lon"] = response["location"]["lon"]
	df.loc[i,"country"] = response["location"]["display_name"].split(", ")[-1]
print(df)
gdf = geopandas.GeoDataFrame(
    df, geometry=geopandas.points_from_xy(df.lon, df.lat))
	
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))

# We restrict to South America.
ax = world.plot(
    color='white', edgecolor='black')

# We can now plot our ``GeoDataFrame``.
gdf.plot(ax=ax, color='red')

plt.savefig("map.png")

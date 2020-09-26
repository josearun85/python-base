# Build an API server
# Flask to build an API
from flask import Flask, request
import json
# geocoding imports
from geopy.geocoders import Nominatim
import time
from pprint import pprint


app=Flask(__name__)
app_geo = Nominatim(user_agent="tutorial")


@app.route("/geocode",methods=["POST"])	
def getlatlon():
	print("Received request:",request.json)
	
	location = app_geo.geocode(request.json["query"]).raw
	return json.dumps({"location":location}),200
	
	
print("This is my server")

if __name__ == "__main__":
	app.run()
	
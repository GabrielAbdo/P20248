"""
7.

"""




import requests  #may need download
import json

api_path = "https://api.nasa.gov/neo/rest/v1/feed?start_date=2021-10-01&end_date=2021-10-08&api_key=DEMO_KEY"

response = requests.get(api_path).text

dict = json.loads(response)


dict
d = dict['near_earth_objects']

names = []
hazardList = []
maxV = 0
maxD = 0

for day in d:
    for asteroid in d[day]:
        asteroid
        name = asteroid["name"]
        velocity = float(asteroid['close_approach_data'][0]['relative_velocity']['kilometers_per_second'])
        distance = asteroid['estimated_diameter']['kilometers']['estimated_diameter_max']
        hazardous = asteroid['is_potentially_hazardous_asteroid']
        names.append(name)

        if velocity > maxV:
            maxV = velocity
            maxVname = name

        if distance > maxD:
            maxD = distance
            maxDname = name

        if hazardous:
            hazardList.append(name)

hazardList = list(set(hazardList))
print("Asteroid Number:", len(names))
print("Hazardous Asteroids:" , len(hazardList))
print("Max Velocity was " + str(maxV) + " from " + maxVname + " Asteroid (km/s)")
print("Max Diameter was " + str(maxD) + " from " + maxDname + " Asteroid (km)")


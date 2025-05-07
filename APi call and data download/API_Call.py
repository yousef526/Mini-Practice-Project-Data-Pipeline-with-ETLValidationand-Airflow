import requests
import json
import os



response = requests.get(url=f"https://disease.sh/v3/covid-19/countries")
#print(response.json())


with open("data.json","w") as f1:
    json.dump(indent=4,obj=response.json() ,fp=f1)
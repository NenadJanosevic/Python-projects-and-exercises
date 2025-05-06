import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "nenadjanosevic"
TOKEN = "asdasfadsfs"
GRAPH_ID = "graph1"
DATE = "20250407"  

user_params = {
     "token": "asdasfadsfs",
     "username": "nenadjanosevic",
     "agreeTermsOfService": "yes",
     "notMinor": "yes"
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
     "id":GRAPH_ID,
     "name":"Cycling graph",
     "unit":"KM",
     "type":"float",
     "color":"ajisai",
     "timezone": "Europe/Belgrade"
}

heders = {
    "X-USER-TOKEN": TOKEN,

}

# response  = requests.post(url = graph_endpoint, json=graph_config,headers=heders)

pixel_creationendpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
     "date":today.strftime("%Y%m%d"),
     "quantity": input("How many Km did you cycle?")
}

response = requests.post(url=pixel_creationendpoint,json=pixel_data,headers=heders)
print(response.text)

pixel_uppdatendpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"

pixel_uppdateData = {
    "quantity":"12"
}

# resposne = requests.put(url=pixel_uppdatendpoint,json=pixel_uppdateData,headers=heders)
# print(resposne.text)

pixel_delet = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=pixel_delet,headers=heders)
# print(response.text)
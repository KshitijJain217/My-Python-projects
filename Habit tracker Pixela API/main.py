import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "" #create new
TOKEN = "" #create new

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# for creating a new user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph01", #create new
    "name": "Workout Graph",
    "unit": "minutes",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
# see your graph using https://pixe.la/v1/users/username/graphs/graphID.html

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph01"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "60",
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph01/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "50"
}

response = requests.put(url=pixel_update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)

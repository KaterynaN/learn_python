import requests
from datetime import date

USERNAME = 'kateryna1982'
TOKEN = '123456qwertyuiop'
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"


user_params = {
    "token": '123456qwertyuiop',
    "username": 'kateryna1982',
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#create user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#create graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

#create pixel (write to graph some data)
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = date.today().strftime("%Y%m%d")
print(today)
pixel_data = {
    "date": today,
    "quantity": "7.5"
}

# response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
# print(response.text)
# print(response.status_code)

#update_pixel
update_date = date.today().strftime("%Y%m%d")
update_pixel_endpoint = f"{pixel_endpoint}/{update_date}"
update_pixel_data = {
    "quantity": "7.5"
}
# response = requests.put(url=update_pixel_endpoint, json=update_pixel_data, headers=headers)
# print(response.text)

#delete pixel
delete_date = date(year=2024, month=9, day=14).strftime("%Y%m%d")
response = requests.delete(url=update_pixel_endpoint, headers=headers)
print(response.text)
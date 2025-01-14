import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

params = {
    "token": "thisisatoken",
    "username": "thisisusername52",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=params)
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{params['username']}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Reading Graph",
    "unit": "pages",
    "type": "int",
    "color": "ajisai",
}
# response = requests.post(
#     url=graph_endpoint, json=graph_config, headers={"X-USER-TOKEN": params["token"]}
# )
entry_endpoint = f"{graph_endpoint}/{graph_config['id']}"

entry_data = {
    "date": datetime.now().strftime("%Y%m%d"),
    "quantity": "10",
}

# response = requests.post(
#     url=entry_endpoint, json=entry_data, headers={"X-USER-TOKEN": params["token"]}
# )
# print(response.text)

response = requests.put(
    url=f"{entry_endpoint}/{datetime.now().strftime("%Y%m%d")}",
    headers={"X-USER-TOKEN": params["token"]},
    json={"quantity": "11"},
)

print(response.text)

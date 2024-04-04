import requests

# Fictional data used for demonstration purposes

# https://pixe.la/@your_username

parameters = {
    "token": "your_token",
    "username": "your_username",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url="https://pixe.la/v1/users", json=parameters)
print(response.text)

graph_parameters = {
    "id": "graph1",
    "name": "Programming Hours",
    "unit": "hours",
    "type": "int",
    "color": "sora",
}

header = {
    "X-USER-TOKEN": "your_token"
}

graph_response = requests.post(url="https://pixe.la/v1/users/your_username/graphs", json=graph_parameters, headers=header)
print(graph_response.text)

pixel_parameters = {
    "date": "20240404",
    "quantity": "2",
}

pixel_response = requests.post(url="https://pixe.la/v1/users/your_username/graphs/graph1", json=pixel_parameters, headers=header)
print(pixel_response.text)
import requests
import datetime as dt

# Nutritionix API
App_Id = "id"
App_Key = "key"

Api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {"content-type": "application/json", "x-app-id": App_Id, "x-app-key": App_Key}
parameters = {"query": input("Tell me which exercises you did: ")}
response = requests.post(url=Api_endpoint, headers=headers, json=parameters)

# print(response.status_code)
print(response.json())

for item in range(len(response.json()["exercises"])):
    exercise = response.json()["exercises"][item]["name"]
    duration = response.json()["exercises"][item]["duration_min"]
    calories = response.json()["exercises"][item]["nf_calories"]
    # print(exercise)

    # sheety API
    sheet_endpoint = "sheets_endpoint"
    workout_parameters = {
        "workout": {
            "date": dt.datetime.now().strftime("%d/%m/%Y"),
            "time": dt.datetime.now().strftime("%H:%M:%S"),
            "exercise": exercise.title(),
            "duration": duration,
            "calories": calories,
        }
    }
    sheet_response = requests.post(url=sheet_endpoint, json=workout_parameters)
    print(sheet_response.status_code)
    print(sheet_response.json())

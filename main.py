#https://www.nutritionix.com/business/api

import requests
import datetime as dt

time_today = dt.datetime.today()
today = time_today.strftime("%d/%m/%Y")
time = dt.datetime.now().strftime("%X")

APP_ID = "175464d1"
API_KEY = "df2286622fd7c13f159c3b48671cb111"
USER_ID = "aliujx"

bearer_headers = {
    "Authorization": "aegv234jvefnlsfg.slrgmbaqwhqveqwcrh3gr"
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_test = input("Which exercises did you do today?: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
query = "ran 2 miles and walked for 3 hours"
my_parameters = {
    "query": exercise_test,
    "gender": "female",
    "weight_kg": 59,
    "height_cm": 167,
    "age": 33
}

responce = requests.post(url=exercise_endpoint, headers=headers, json=my_parameters)
exercise_list = responce.json()["exercises"]
#print(exercise_list)
exercise = exercise_list[0]["name"]
duration = exercise_list[0]["duration_min"]
calories = exercise_list[0]["nf_calories"]
#print(exercise, calories, duration)

sheet_endpoint = "https://api.sheety.co/f34af4f8a2689c02a3b0a6c031898be8/workoutTracking/лист1"

parameters = {
    "date": today,
    "time": time,
    "exercise": exercise,
    "duration": duration,
    "calories": calories
}
response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()


for exercise in exercise_list:
    sheet_inputs = {
        "лист1": {
            "date": today,
            "time": time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=bearer_headers)

    print(sheet_response.text)

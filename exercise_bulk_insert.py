
import requests

exercise_url = 'http://127.0.0.1:8000/gym/exercise/'

'''new_row = {'exercise_name': '400 meter sprints',

    'exercise_category': 'cardio',

    'exercise_recommended_weight': 0,

    'exercise_recommended_sets': 4,

    'exercise_recommended_reps': 0,

    'exercise_recommended_interval': 80}

x = requests.post(exercise_url, params= new_row) #this uses the post method to print the params'''

'''Inserts users in a dictionary format where key is the field and value is the data'''

#x = requests.delete(f'{exercise_url}3')#delete specific data, the number is the id

#update specific rows
updated_row = {'exercise_recommended_reps': 10, 'exercise_recommended_weight': 155}# this is the attributes you want to change
x = requests.put(f'{exercise_url}2', params = updated_row)#number after exercise_url is exercise_id

#x = requests.get(exercise_url)#get all data

#x = requests.get(f'{exercise_url}400 meter sprints')#get specific data

print(x.text) #prints this in terminal


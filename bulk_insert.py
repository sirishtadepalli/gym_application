'''This is another way of adding rows.'''
import requests

'''This is found in the API '''
user_url = 'http://127.0.0.1:8000/gym/users/' #get user_url of route but delete everything fr
exercise_url = 'http://127.0.0.1:8000/gym/exercise/'
equipment_url = 'http://127.0.0.1:8000/gym/equipment/'

#new_row = {'username': 'Izzy', 'email': 'izzy@gmail.com', 'mobile_number': 1111111111, 'weight' : 45, 'height': 24, 'body_fat_percentage': 9}
new_row = {'name' : 'deadlift mat', 'brand' : 'power fit', 'cost' : 45.99}
x = requests.post(equipment_url, params= new_row)
#x = requests.post(user_url, params= new_row) #post new users



#new_row = {'username': 'Izzy', 'email': 'izzy@gmail.com', 'mobile_number': 1111111111, 'weight' : 45, 'height': 24, 'body_fat_percentage': 9}
#x = requess.post(user_url, params= myobj) #post new users

'''Inserts users in a dictionary format where key is the field and value is the data'''

#x = requests.delete(f'{user_url}3')#delete specific data, the number is the id

#updated_row = {'active' : True}
#x = requests.put(f'{user_url}2', params = updated_row)#update specific user, number after user_url is id

#x = requests.get(user_url)#get all data

#x = requests.get(f'{user_url}4')#get specific data

print(x.text) #prints this in terminal


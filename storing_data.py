import json
import requests

# numbers = [2, 3, 5, 7, 11, 13]
#
# filename = '/Users/raulgiron/Desktop/TeamTreeHouse/TeamTreeHouse-ObjectOrientedPython/numbers.json'
# with open(filename, 'w') as file_object:
#     json.dump(numbers, file_object)
#
# with open(filename, 'r') as file_object:
#     numbers = json.load(file_object)
#
# print(numbers)
#
#
# filename = '/Users/raulgiron/Desktop/TeamTreeHouse/TeamTreeHouse-ObjectOrientedPython/username.json'
#
# try:
#     with open(filename, 'r') as file_object:
#         username = json.load(file_object)
# except FileNotFoundError:
#     username = input(f"What is your name? ")
#     with open(filename, 'w') as file_object:
#         json.dump(username.title(), file_object)
#         print(f"we'll remember you when you came back, {username.title()}!")
# else:
#     print(f"Welcome back, {username}!")

filename = '/Users/raulgiron/Desktop/TeamTreeHouse/TeamTreeHouse-ObjectOrientedPython/incremental.json'

try:
    with open(filename, 'r') as file_object:
        counting = json.load(file_object)
except FileNotFoundError:
    counting = 0
    with open(filename, 'w') as file_object:
        json.dump(counting, file_object)
        print(f"A file was created with the following number: {counting} ")
else:
    counting += 1
    with open(filename, 'w') as file_object:
        json.dump(counting, file_object)
        print(f"The counter number is: {counting} ")

# Making a get request
filename = '/Users/raulgiron/Desktop/TeamTreeHouse/TeamTreeHouse-ObjectOrientedPython/api_data.json'
response = requests.get("https://api.github.com")
data = response.json()
# print(type(data))  # <class 'dict'>
# print(data)

with open(filename, 'w') as file_object:
    json.dump(data, file_object)

with open(filename, 'r') as file_object:
    git_hub = json.load(file_object)
    print(git_hub)

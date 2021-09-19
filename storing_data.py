import json


numbers = [2, 3, 5, 7, 11, 13]

filename = '/Users/raulgiron/Desktop/TeamTreeHouse/TeamTreeHouse-ObjectOrientedPython/numbers.json'
with open(filename, 'w') as file_object:
    json.dump(numbers, file_object)

with open(filename, 'r') as file_object:
    numbers = json.load(file_object)

print(numbers)

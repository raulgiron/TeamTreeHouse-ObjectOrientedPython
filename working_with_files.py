import json

filename = '/Users/raulgiron/Desktop/TeamTreeHouse/TeamTreeHouse-ObjectOrientedPython/programming.txt'

with open(filename, 'w') as file_object:
    file_object.write(f"I love programming.\n")
    file_object.write(f"\tI love creating new games.\n")
    file_object.write(f"\t\tI also love finding meaning in large datasets.\n")
    file_object.write(f"\t\t\tI love creating apps that can run in a browser.\n")

with open(filename, 'r') as file_object:
    lines = file_object.readlines()
    print(lines)
    file = ''
    for line in lines:
        file += line
print(file)

filename = 'guest.txt'

with open(filename, 'w') as file_object:
    name = input("What is your full name?")
    file_object.write(name)

with open(filename, 'r') as file_object:
    name = str(file_object.readline().title())
    print(name)

filename = 'guest.txt'
index = 0
while True:
    print(f"Press letter 'Q' to exit the program.")
    name = input("What is your full name? ")
    if name.lower() == 'q':
        break
    index += 1
    print(f"Hi, {name.title()}, welcome to the system!")
    with open(filename, 'a') as file_object:
        file_object.write(f'{index}.- {name.title()}\n')

filename1 = '/Users/raulgiron/Desktop/TeamTreeHouse/TeamTreeHouse-ObjectOrientedPython/programming.txt'
filename2 = '/Users/raulgiron/Desktop/TeamTreeHouse/TeamTreeHouse-ObjectOrientedPython/incremental.json'

while True:
    print(f"Press letter 'Q' to exit the program.")
    name = input("What's your name? ")
    if name.lower() == 'q':
        break
    answer = input("Why do you like computer programming? ")
    if answer.lower() == 'q':
        break
    try:
        with open(filename2, 'r') as file_object:
            counting = json.load(file_object)
    except FileNotFoundError:
        counting = 1
        with open(filename2, 'w') as file_object:
            json.dump(counting, file_object)
            print(f"A file was created with the following number: {counting} ")
    else:
        counting += 1
        with open(filename2, 'w') as file_object:
            json.dump(counting, file_object)
            print(f"The counter number is: {counting} ")
    try:
        with open(filename1, 'r') as file_object:
            lines = file_object.readlines()
            file = ''
            for line in lines:
                file += line
            print(file)
    except FileNotFoundError:
        with open(filename1, 'w') as file_object:
            file_object.write(f"{counting}-) Hi {name.title()}! Why do you like computer programming?\n")
            file_object.write(f"    {counting}.- {answer}\n\n")
    else:
        with open(filename1, 'a') as file_object:
            file_object.write(f"{counting}-) Hi {name.title()}! Why do you like computer programming?\n")
            file_object.write(f"    {counting}.- {answer}\n\n")

with open(filename1, 'r') as file_object:
    encuestados = file_object.readlines()
    for encuestado in encuestados:
        print(encuestado.strip())

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


filename = "Alice's Adventures in Wonderland.txt"

filenames = ["Moby Dick.txt", "Siddhartha.txt", "Little Women.txt", "Alice's Adventures in Wonderland.txt"]


def count_words(file_name, f_word=''):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.\n")
        # Not recommended just for learning purposes.
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words:,} words.")
        if f_word:
            h_words = contents.lower().count(f_word)
            print(f"\t- The word '{f_word}' appears {h_words:,} times in the book.\n")


for filename in filenames:
    count_words(filename, 'the')

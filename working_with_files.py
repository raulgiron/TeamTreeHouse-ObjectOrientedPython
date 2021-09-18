# filename = '/Users/raulgiron/Desktop/TeamTreeHouse/TeamTreeHouse-ObjectOrientedPython/programming.txt'
#
# with open(filename, 'w') as file_object:
#     file_object.write(f"I love programming.\n")
#     file_object.write(f"\tI love creating new games.\n")
#     file_object.write(f"\t\tI also love finding meaning in large datasets.\n")
#     file_object.write(f"\t\t\tI love creating apps that can run in a browser.\n")
#
# with open(filename, 'r') as file_object:
#     lines = file_object.readlines()
#     print(lines)
#     file = ''
#     for line in lines:
#         file += line
# print(file)

# filename = 'guest.txt'
#
# with open(filename, 'w') as file_object:
#     name = input("What is your full name?")
#     file_object.write(name)
#
# with open(filename, 'r') as file_object:
#     name = str(file_object.readline().title())
#     print(name)

# filename = 'guest.txt'
# index = 0
# while True:
#     print(f"Press letter 'Q' to exit the program.")
#     name = input("What is your full name? ")
#     if name.lower() == 'q':
#         break
#     index += 1
#     print(f"Hi, {name.title()}, welcome to the system!")
#     with open(filename, 'a') as file_object:
#         file_object.write(f'{index}.- {name.title()}\n')

filename = '/Users/raulgiron/Desktop/TeamTreeHouse/TeamTreeHouse-ObjectOrientedPython/programming.txt'
counter = '/Users/raulgiron/Desktop/TeamTreeHouse/TeamTreeHouse-ObjectOrientedPython/incremental.txt'

while True:
    with open(filename, 'a') as file_object:
        print(f"Press letter 'Q' to exit the program.")
        name = input("What's your name? ")
        if name.lower() == 'q':
            break
        question = "Why do you like computer programming? "
        print(question)
        answer = input("Please type your answer: ")
        if answer.lower() == 'q':
            break
        file_object.write(f"{numbers}.- Hi {name.title()}! {question}\n")
        file_object.write(f"   * {answer}\n\n")
    with open(filename, 'r') as file_object:
        lines = file_object.readlines()
        # print(lines)
        file = ''
        for line in lines:
            file += line
        print(file)

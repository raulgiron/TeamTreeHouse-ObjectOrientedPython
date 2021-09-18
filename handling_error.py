from termcolor import colored

while True:
    try:
        print("TYPE TWICE ZERO -00- TO QUIT THE PROGRAM!")
        dividend: int = int(input(colored("Please type -dividend- number: ", 'blue')))
        if int(dividend) == 999:
            break
    except ValueError:
        print(colored(f"WARNING: - Dividend must be a number.\n \t * Please type a number no a letter.", 'red'))
        continue
    try:
        divisor: int = int(input(colored("Please type -divisor- number: ", 'magenta')))
        if int(divisor) == 999:
            break
    except ValueError:
        print(colored(f"WARNING: - Divisor must be a number.\n \t * Please type a number no a letter.", 'red'))
        continue
    try:
        quotient: float = float(dividend / divisor)
        print(f"{dividend} / {divisor} = {quotient:,}")
    except ZeroDivisionError:
        print(f"\tYou can't divide by zero!")

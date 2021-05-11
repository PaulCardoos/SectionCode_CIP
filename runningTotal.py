"""
Prompts the user to enter numbers and prints
the running total until the user enters 0.
"""

BREAK_CONDITION = 0

def main():
    n = int(input("Enter a value: "))
    total = 0

    while n != BREAK_CONDITION:
        total += n
        print("Running total is", total)
        print("")
        n = int(input("Enter a value: "))      

if __name__ == '__main__':
    main()
"""
Prints the Fizz Buzz sequence up to a given number.
"""
# if divisible by 3 fizz
# if divisble by 5 buzz
#if the number is 3 or 5 fizzzbuzz


def check_for_three_and_five(number):
     if number % 5 == 0 and number % 3 == 0:
         return True
     return False

def check_for_three(number):
    return number % 3 == 0

def check_for_five(number):
    return number % 5 == 0

def main():
    N = int(input("Number to count to: "))
    fizz = 0
    buzz = 0
    fizzBuzz = 0

    #loop to N
    for i in range(1, N + 1):
        #check for 3 and 5
        if check_for_three_and_five(i):
            print("Fizzbuzz")
            fizzBuzz += 1
        elif check_for_three(i):
            print("Fizz")
            fizz += 1
        elif check_for_five(i):
            print("Buzz")
            buzz += 1
        else:
            print(i)
    
    print("Num fizzed:", fizz) 
    print("Num buzzed:", buzz) 
    print("Num fizzbuzzed:", fizzBuzz) 

    
if __name__ == '__main__':
    main()
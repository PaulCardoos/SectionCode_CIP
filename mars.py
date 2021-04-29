"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""
#on mars you are 37.8% of your weight on earth
MARS_CONVERSION = .378

def main():
    #input comes in as a str
    weight = input(str("Enter a weight on Earth : "))

    #convert string input to float and multiply it by conversion to get mars weight
    mars_weight = float(weight) * MARS_CONVERSION

    #convert back to string to concatenate and print out result
    print("The equivalent on Mars : " + str(mars_weight))

if __name__ == "__main__":
    main()
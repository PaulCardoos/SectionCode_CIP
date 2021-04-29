"""
Simulates a magic eight ball.
Prompts the user to type a yes or no question and gives
a random answer from a set of prefabricated responses.
"""
#we need to import random here in order to generate a random index for our responses
import random

#our responses are global meaning we can access them from anywhere in the code
responses = [
    "As I see it, yes.", 
    "Outlook good", 
    "It is decidedly so.", 
    "Most likely",
    "Concentrate and ask again.",
    "Don't count on it.",
    "It is certain",
    "The reply is no.",
    "Outlook not so good",
    "Reply hazy, try again.",
    "Signs point to yes",
    "Very doubtful",
    "Without a doubt.",
    "Yes.",
    "Yes - definetly",
    "You may rely on it"
    ]

def main():
    #input user question
    question = input(str("What is your question? : "))
    #this line of code generate a random index from numbers 0 to the length of responses list
    random_index = random.randint(0, len(responses))
    #return a responses with the random index
    print(responses[random_index])  

if __name__ == "__main__":
    main()

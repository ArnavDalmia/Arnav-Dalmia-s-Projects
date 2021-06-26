print("Welcome to Rock, Paper and scissors. I will be your opponent.")
b = input("Do you want to play rock paper scissors? ")
while b == ("yes"):
    import random
    c = ['rock', 'paper', 'scissors']
    c = random.choice(c)
    print("Are you ready?")
    u = input("Rock paper scissors shooh : ")

    if c == u:
        print("Draw")
    
    if c == ("rock")and u == ("paper"):
        print(" You win I chose rock")

    if c == ("rock")and u == ("scissors"):
        print("You lose I chose rock")

    if c == ("paper")and u == ("rock"):
        print("You lose I chose paper")

    if c == ("paper")and u == ("scissors"):
        print("You win I chose paper")

    if c == ("scissors")and u == ("paper"):
        print("You lose I chose scissors")
    
    if c == ("scissors")and u == ("rock"):
        print("You win I chose scissors")

    yn = input("Do you want to play again? ")
    if yn == ("yes"):
        b = ("yes")

    if yn == ("no"):
        b = ("no")
        print("Goodbye!")
    





    

    


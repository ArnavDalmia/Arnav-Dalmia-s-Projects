def sc():
    f = input("Enter your first number with no spaces: ")
    s = input("Enter your second number with no spaces: ")
    o = input("Enter your operation with no spaces, make sure that it looks like\" +,-,*,/\" :")

    f = float(f)
    s = float(s)

    if (o) == ("+"):
        print (f + s)

    if (o) == ("-"):
        print (f - s)

    if (o) == ("*"):
        print (f * s)

    if (o) == ("/"):
        d = input("Do you want deciamls in your answer?")
        if d == ("yes"):
            print(f / s)
        elif d == ("no"):
            print(("The quotient is ") + str(round(f // s)) + (", and the remainder is ") + str(round(f % s)) + ("."))
        else:
            print("Invalid word : please use either yes or no.")

def main():
    u = input("Do you want to use the simple calculator? ")
    while u == ("yes"):
        sc()

        
        value_for_u_change = input("Would you like to perform another calculation? ")
        if value_for_u_change == ("yes"):
            u = ("yes")
        if value_for_u_change == ("no"):
            u = ("no")
        
    if u == ("no"):
        print("Thank you for using the simple calculator.")
        print("AD inc. TM")
        quit

main()    
    

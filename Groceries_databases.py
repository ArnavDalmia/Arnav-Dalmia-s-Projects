import os
import sys
import time
infinite = str('∞')

class item:
    name = ""
    description = ""
    quantity = None

    def __init__(self, iName, iDescription, iQnt):
        self.name = iName
        self.description = iDescription
        self.quantity = iQnt

    def prtItem(self):
        print(self.name, self.description, self.quantity)



#function Definitions

#Part 1 Functions

def msgStartup():
    print("Welcome to the Father's day market! We have many gifts for you, but first:")

def sayHi():
    name =input("\nWhat is your name?\n")
    os.system('cls')
    print("Hello " + name + ", what would you like today?")


#Menue Funtions
def mainMenu():
    prtHeader(" Main Menu ")
    cont = False
    options = (1,2,3,9) 
    while not cont:
        num = input("Please select an Option\n1. Tech\n2. Appliances\n3. Hardware\n9. Exit\n")
        if ValidateInt(num, options):
            num = int(num)
            cont = True
        else:
            os.system('cls')
            print("Invalid input")

    return num

def tech(): 
    prtHeader(" Tech ")
    v1 = item("1. Power Bank", ",item price: ", "$20")
    v2 = item("2. Monitor", ",item price: ", "$150")
    v3 = item("3. Computer", ",item price: ", "$999")
    v4 = item("4. Sony OLED TV", ",item price: ", "$1999")
    v5 = item("5. Sony Audio System", ",item price: ", "$4")
    v6 = item("6. Laptop", "tech item, price: ", "$")
    v7 = item("7. Automatic Garbage bag tyer", ",item price: ", "$")
    v8 = item("8. Iphone 12", ",item price: ", "$")
    v9 = item("9. Samsung S21", ",item price: ", "$")
    ourTech = [v1, v2, v3, v4, v5, v6, v7, v8, v9]
    print("These are the tech items we have: \n")
    print("".center(50,"-"))
    printList(ourTech)
    print("".center(50,"-"))

    tech_purchase = input("Would you like to purchase anything today from the Tech aisle? (y/n) ")
    if tech_purchase == ("y"):
      selection = input("What is the item number of your selection? ")
      selection = int(selection)
      if (selection > 9 or selection < 1):
        print("You have selected an invalid option, relaunch the program to retry. BYE BYE")
        os.system('cls')
        sys.exit()
      cashier(selection)
    elif tech_purchase == ("n"):
      input("\nPress Enter to return to the previous menu")
      os.system('cls') 
    else:
      print("You have selected an invalid option. If you wish to purchase something type 'y'.")
      input("\nPress Enter to return to the previous menu")
      os.system('cls')


    
def appliances():
    prtHeader(" Appliances ")
    f1 = item("1. Juicer" , ",item price: ", "200$") 
    f2 = item("2. Coffee Brewer", ",item price: ", "150$") 
    f3 = item("3. Cocoa Bean Grinder", ",item price: ", "125$")
    f4 = item("4. Portable Stove", ",item price: ", "180$")
    f5 = item("5. Grill / Barbeque", ",item price: ", "460$")
    f6 = item("6. Japanese Knife Set", "tech item, price: ", "360$")
    f7 = item("7. Liquor stands", ",item price: ", "95$")
    ourApp = [f1, f2, f3, f4, f5, f6, f7]
    print("These are the applicances we have: \n")
    print("".center(50,"-"))
    printList(ourApp)
    print("".center(50,"-"))

    app_purchase = input("Would you like to purchase anything today from the Appliances aisle? (y/n) ")
    if app_purchase == ("y"):
      selection = input("What is the item number of your selection? ")
      selection = int(selection)
      if (selection > 7 or selection < 1):
        print("You have selected an invalid option, relaunch the program to retry. BYE BYE")
        os.system('cls')
        sys.exit()
      cashier(selection)
    elif app_purchase == ("n"):
      input("\nPress Enter to return to the previous menu")
      os.system('cls') 
    else:
      print("You have selected an invalid option. If you wish to purchase something type 'y'.")
      input("\nPress Enter to return to the previous menu")
      os.system('cls')


def hardware():
    prtHeader(" Hardware ")
    b1 = item("1. Lawnmower", ",item price: ", "300$")
    b2 = item("2. Weed Whacker", ",item price: ", "260$")
    b3 = item("3. Garden Tools", ",item price: ", "75$")
    b4 = item("4. Leaf Blower", ",item price: ", "120$")
    b5 = item("5. Snow Blower", ",item price: ", "200$")
    b6 = item("6. Toolbox", "tech item, price: ", "150$")
    b7 = item("7. Tire Jack", ",item price: ", "100$")
    b8 = item("8. Air Pump", ",item price: ", "60$")
    b9 = item("9. Wheel Patch Kit", ",item price: ", "160$")
    ourHar = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
    print("These are the hardware items we have: \n")
    print("".center(50,"-"))
    printList(ourHar)
    print("".center(50,"-"))

    har_purchase = input("Would you like to purchase anything today from the Hardware aisle? (y/n) ")
    if har_purchase == ("y"):
      selection = input("What is the item number of your selection? ")
      selection = int(selection)
      if (selection > 7 or selection < 1):
        print("You have selected an invalid option, relaunch the program to retry. BYE BYE")
        os.system('cls')
        sys.exit()
      cashier(selection)
    elif har_purchase == ("n"):
      input("\nPress Enter to return to the previous menu")
      os.system('cls') 
    else:
      print("You have selected an invalid option. If you wish to purchase something type 'y'.")
      input("\nPress Enter to return to the previous menu")
      os.system('cls')

#Helper Functions

def ValidateYorN(entry):
    result = False
    if entry.lower() == "y" or entry.lower() == "n":
        
        result = True
    return result

def ValidateInt(entry, values):
    result = False
    
    if entry.isdigit():
        if int(entry) in values:
            result = True
    return result

def printList(items):
    
    for item in items:
        item.prtItem()
        
def prtHeader(strHeader):
    print("".center(50,"#"))
    print(strHeader.center(50,"@"))
    print("".center(50,"#"))

def cashier(selection):
  os.system('cls')
  print("\nYou chose item number " + str(selection) + ". Thank you for shopping your item will be delivered to your billing address in 5-7 business days. ")
  print("\nThis window will close in 5 seconds.")
  time.sleep(6)
  sys.exit()
    
#main code


msgStartup()
sayHi()

#Main Menu code (when selecting either tech, hardware or appliances, list will appear)

while True:
    selection = mainMenu()
    os.system('cls')
    

    if selection == 1:
      tech()
      os.system('cls')
    elif selection == 2:
      appliances()
      os.system('cls')
    elif selection == 3:
      hardware()
      os.system('cls')
    elif selection == 9:
      cont = False
      confirm = False
      while not cont:
          print("Thank you for shopping at Father's Day Market. To exit press y, or n to return to menu.")
          YN = input()
          if ValidateYorN(YN):  
            cont = True
            if YN.lower() == 'y':
              confirm = False
              os.system('cls')
              sys.exit()
            elif YN.lower() == 'n':
              confirm = True
              os.system('cls')
              input("\nPress Enter to return to the previous menu")
          else:
            confirm = True
            print("You have selected an invalid input. Please relaunch the program.")
            time.sleep(6)
            os.system('cls')
            sys.exit()

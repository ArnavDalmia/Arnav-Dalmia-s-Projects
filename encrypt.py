# This is the Encryption/Decryption program. It encrypts/decrypts a user's message with a user inputted key. It only encrypts letters in both capital and lower case, so it avoids all punctuation and numbers.
# Made for ICS3U1-03, by Arnav Dalmia
# class used: colours   This class was created by Emidio DiAntonio for ICS3U1-03, it allows the usage of colours in programs when used

# functions 
# isInteger              This function will return True if a string is an integer or False if not
# inputInteger           This function will call the isInteger function to verify if a user's input is an integer. It will continue to ask the user for a valid integer input and then it will return the integer input
# inputIntegerBetween    This function will call the inputInteger function and verify if the users inputted integer is between a lower bound and higher bound value. If it does not meet the requirments then the user will be returned a error message informing them that the value is either too high or low and will tell them the number requirments. It will repeat until a valid integer is entered
# encrypt                This function will decide whether to encrypt or decrypt. After so it will ask for the user's encryption key, as well as their message. It will then return back the new message.
# dispMessage            This function will display the new Encrypted/Decrypted message after the encrypt has been called

# --------------------------- Local Variables ---------------------------
# isInteger(string)
# string     This variable contains a string value that will be checked to be a integer

#inputInteger(message)
# message   This string variable contains the message that will be asked of the user
# invalidInput  This boolean variable is used to verify if a input is a valid integer variable. Until invalidInput = False, then the loop will continue to ask for a valid integer 
# result    This variable contains the result of the user's input to message

# inputIntegerBetween(message, lowBound, highBound)
# message   This string variable contains the message that will be asked of the user
# lowBound   This integer variable represents the low bound of the user's integer input, it ensures that the user's input fits the requirement
# highBound     This integer variable represents the high bound of the user's integer input, it ensures that the user's input fits the requirement
# invalidInput  This boolean variable is used to verify if a input is a valid integer variable. Until invalidInput = False, then the loop will continue to ask for a valid integer 
# result    This variable contains the result of the user's input to message

# encrypt(status)
# status    boolean variable that is used to determine whether the function will be used to encrypt or decrypt
# key   This integer variable contains the encryption key number so that the function knows how much to encrypt by 
# string    This string variable contains the users message that they wish to encrypt/decrypt
# newString This string variable contains the users message that is either encrypted or decrypted
# i     This is an iterable variable that individually holds the characters of string
# value     This integer variable contains the ASCII value of the character of i 
# new_val   This integer variable contains the encrypted ASCII value of the character i 
# ****************************** A, a, Z, z documented underneath

# dispMessage(message, method)
# message   string variable that contains the encrypted/decrypted message of the user 
# method    integer variable that is used to determine if the message is to be displayed as an encryption or decryption(using colours and certain phrasing)

#---------------------------Main Variables used ---------------------------
# a     integer value containing the ASCII value of the letter a
# A     integer value containing the ASCII value of the letter A
# z     integer value containing the ASCII value of the letter z
# Z     integer value containing the ASCII value of the letter Z
# quit  boolean variable that is used to ensure that the menu options are repeated until it is True, and then the quit message will be displayed
# option    integer return value of inputIntegerBetween(), contains the users choice from the 3 menu options
# message   string variable containing the return of the encrypt function, is the new message after being encrypted/decrypted


# --------------------------- MAIN -----------------------------

a = ord("a") #setting base integer variables to be used
z = ord("z")
A = ord("A")
Z = ord("Z")

class colours:
    reset='\033[0m'
    bold='\033[01m'
    underline='\033[04'
    class fg:
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
    class bg:
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'
def isInteger(string): #returns True or False depending if a number is an integer
    try:
        int(string)
        return True
    except ValueError:
        return False
def inputInteger(message):#asks user for input and validates if it is an integer. Continusly asks until vaild input is given. In the end returns valid integer
    invalidInput=True
    while invalidInput:
        result = input(message)
        if isInteger(result): #uses isInteger to verify if integer 
            result = int(result)
            invalidInput = False
        else: 
            print(colours.bg.red+"Please enter a valid integer value"+colours.reset)#outputs error message in red highlight
    return result 
def inputIntegerBetween(message,lowBound,highBound):
    invalidInput = True
    while invalidInput:
        result = inputInteger(message)
        if result < lowBound: 
            print("Please enter a value larger than or equal to ",lowBound)#error message if user input is less than lowerbound
        elif result > highBound: 
            print("Please enter a value smaller than or equal to ",highBound)#error message if user input is greater than higherbound
        else: 
            invalidInput = False #if all conditions are met, the loop terminates
    
    return result # returns the validated user input 
def encrypt(status):
    if status == True: #checks the condition, which dictates if the function will be used to encrypt or decrypt, in the case of True, then encrypt
        print(colours.bg.red+"Encryption Mode Activated"+colours.reset) #prints message 
        key = inputIntegerBetween("Please enter the encryption key (an integer between 1 and 5): ", 1, 5) # asks for encryption key between 1 and 5
        string = input("Type in your message: ") # asks for message 
        newString = "" # creates empty string to iterate through old message and add to 
        for i in string: # uses for looping, and uses "i" as individually encrypting characters 
            value = ord(i) # establishes the ASCII value of i(character in string)
            if (value <= z and value >= a) or (value<= Z and value >= A): # This condition is to verify that the character indeed is a letter. Above A,a,z,Z were set to their ASCII values, so comparing i to these values lets the program understand if i is a character
                new_val = value + key # establishes that the encrypted value of the character is stored in the integer variable new_val
                if (value <= Z) and (new_val > Z): # if the value of i is less than Z and the new_val > Z, this means that i is a capital letter that is between A and Z, and that if after the encryption it exceeds Z
                    new_val = A + (new_val-(Z+1)) # this will wrap around the Z and go back to A, as a way to ensure that any captial letter remains captialized
                elif (value >= a) and (new_val > z): # if the value of i is greater than a and new_val > z, this means that i is a lowercase letter between a-z, but after the encryption it exceeds z
                    new_val = a + (new_val - (z+1)) # this will wrap around the z and go back to a, as a way to ensure that any letter that is lower case, will remain that way
                # if their is no problem with the new_val exceeding Z or z, then the new_val will simply be the key + value. 
                newString += chr(new_val) #After new_val has been calculated, the character equivalence is added to the newString using the chr() function
            else: # if i is not a letter, then newString adds the original character back into the same position 
                newString += chr(value)
        return newString # after the encryption process is finished, the newString, the encrypted, is returned
    
    else: # if status is not True, then Decryption mode is activated, and this function will decrypt
        print(colours.bg.cyan+"Decryption Mode Activated"+colours.reset)#prints message
        print(colours.bg.orange + "Warning: You should only decrypt messages if you know it is safe to do so."+ colours.reset)
        key = inputIntegerBetween("Please enter the encryption key (an integer between 1 and 5): ", 1, 5)# asks for encryption key between 1 and 5
        string = input("Type in your message: ")# asks for message 
        newString = "" # creates empty string to iterate through old message and add to
        for i in string:
            value = ord(i) # establishes the ASCII value of i(character in string)
            if (value <= z and value >= a) or (value<= Z and value >= A):# This condition is to verify that the character indeed is a letter. Above A,a,z,Z were set to their ASCII values, so comparing i to these values lets the program understand if i is a character
                new_val = value - key # establishes that the encrypted value of the character is stored in the integer variable new_val
                if (value <= Z) and new_val < A:# if the value of i is less than Z and the new_val < A, this means that i is a capital letter between A-Z but when the decryption is applied it goes past the ASCII's of letters
                    new_val = Z+1 - (A - new_val) # this will wrap around the A and return back to Z, as a way to ensure that when letter are decrypted they remain letters
                elif (value >= a) and new_val < a: # if the value of i is greater than a and the new_val < a, this means that i is a lowercase letter between a-z, but the decryption exceeds a
                    new_val = z+1 - (a - new_val)# this will wrap around the a and return back to z, as a way to ensure that when letter are decrypted they remain letters
                # if their is no problem with the new_val exceeding A or a, then the new_val will simply be the value - key. 
                newString += chr(new_val)#After new_val has been calculated, the character equivalence is added to the newString using the chr() function
            else:# if i is not a letter, then newString adds the original character back into the same position 
                newString += chr(value)
        return newString # after the encryption process is finished, the newString, the encrypted, is returned
def dispMessage(message, method):
    if method == 1: # if the option selected is Encryption
        print(colours.fg.red + "Encrypted Text: ")
        print("----------------")
        print(message + colours.reset)
    else: # if the option selected is Decryption
        print(colours.fg.green + "Unencrypted Text: ")
        print("------------------")
        print(message + colours.reset)        

#prints welcome message 
print(colours.bg.green+ "Welcome to the encryption/decryption program. Provide a phrase to either encrypt or\n decrypt and appropriate addition key.  (c) 2022 CM Software Group"+colours.reset)      

quit = False #commences loop, uses quit varaiable to make sure loop doesnt terminate until quit's value is changed 
while not quit:
    print(colours.fg.yellow+"Encryptomatic Encryption Program Options: \n\t1) Encrypt\n\t2) Decrypt\n\t3) Quit"+colours.reset)#provides options
    option = inputIntegerBetween("Please select a menu option: ", 1, 3)#asks for users choice
    if option == 1: # if the choice is to encrypt
        message = encrypt(True)#calls encrypt function with True parameter, which allows for the message to be properly encrypted 
        dispMessage(message, 1) #displays the encrypted message 
    elif option == 2: # if the choice is to decrypt 
        message = encrypt(False)#calls encrypt function with False parameter, which allows for the message to be properly decrypted
        dispMessage(message, 2)#displas the decrypted message
    else:
        quit = True #ends loop if 3 is inputted, any other values wouldnt pass the option variable as there would be an error for any value that is greater than 3 or lower than 1
print(colours.bg.purple+"Goodbye have a nice day. Don't forget to look for other software titles"+colours.reset)#provides end message
print(colours.bg.purple+"from the CM Software Group."+colours.reset)

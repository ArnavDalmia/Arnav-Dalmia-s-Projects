#Welcome to the Math Integer quiz program. This program was created by Arnav Dalmia and by the instruction of Emidio DAntonio.
# The purppose of this program is to test the users knowledge through integer math questions(addition, subtraction, multiplication, division)

#Functions used:

# isInteger(string)         This function will return True if a string is an integer or False if not
# inputInteger(message)     This function will call the isInteger function to verify if a user's input is an integer. It will continue to ask the user for a valid integer input and then it will return the integer input
# isFloat(string)           This function will return True if a string is a float or False if not
# inputFloat(message)       This function will call the isFloat function to verify if a user's input is an float. It will continue to ask the user for a valid float input and then it will return the float input
# operation(number)         This function will return the symbol of the randomized math operation. Uses the number argument as a radnomized number between 1 and 4 to choose the operation.
# questionColour(symbol)    This function will return the colour of the question depending on the symbol varialb that contains the symbol of the operation that is used
# grade(avg)                This function will check the letter grade using the avg variable and return the lettter variable

# Variables Used:

# questions                 integer variable containing return of the inputInteger function. Containss user's desiered number of questions
# counter                   integer varialbe that is used to ensure that the correct amount of questions are played through boolean while looping
# total                     integer varialbe that contain the total score of the player
# average                   integer variable that contains the user's rounded average
# choices                   integer variable containing random integer between 1-4 for the action of choosing an operation 
# operation_selected        string variable containing the return of the operation function that holds the operation is the form of a string of the integer questions
# colour_of_question        string varialbe containing the colour of the question based on the operation, using questionColour function
# first_number              integer variable containing random number between -10 and 10
# second_number             integer variable containing random number between -10 and 10
# expression                string varialbe containing the full question with colour, numbers and operation
# answer                    integer variable containing the correct answer to the question
# userAnswer                integer variable containing return result of integerInput function asking for the users answer      
# letter                    string varialbe containing the return of grade function, contains the letter grade of the user 
  
import random #imports random library
class colours:
    '''Colors class:
    Reset all colors with colors.reset
    Two subclasses fg for foreground and bg for background.
    Use as colors.subclass.colorname.
    i.e. colors.fg.red or colors.bg.green
    Also, the generic bold, disable, underline, reverse, strikethrough,
    and invisible work with the main class
    i.e. colors.bold
    '''
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
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
        if isInteger(result):
            result = int(result)
            invalidInput = False
        else: 
            print(colours.bg.red+"Please enter a valid integer value"+colours.reset)#outputs error message in red highlight
    return result 
def isFloat(string):#returns True or False depending if a number is an integer
    try:
        float(string)
        return True
    except ValueError:
        return False
def inputFloat(message): #asks user for input and validates if it is a float. Continusly asks until vaild input is given. In the end returns valid float
    invalidInput=True
    while invalidInput:
        result = input(message)
        if isFloat(result):
            result = float(result)
            invalidInput = False
        else: 
            print(colours.bg.red+"Please enter a valid float value"+colours.reset)#outputs error message in red highlight
    return result 
def operation(number):#returns string operation depending on number arguement
    if number == 1:
        return "+" #addition
    elif number == 2:
        return "-"#subtraction
    elif number == 3:
        return "x"#multiplication
    else:
        return "/" # division
def questionColour(symbol): #returns colour of question depending on operation performed
    if symbol == "+":
        color = colours.fg.pink #addition colour
    elif symbol == "-":
        color = colours.fg.yellow # subtraction colour
    elif symbol == "x":
        color = colours.fg.orange # mulitplicatino colour
    else:
        color = colours.fg.lightcyan #division colour
    return color #returns the colour
def grade(avg):#checks for letter equivalence to average and returns character as a string
    if 90 <= avg and avg <= 100:
        return 'A+'
    elif 85 <= avg and avg <= 89:
        return 'A'
    elif 80 <= avg and avg <= 84:
        return 'A-'
    elif 77 <= avg and avg <= 79:
        return 'B+'
    elif 73 <= avg and avg <= 76:
        return 'B'
    elif 70 <= avg and avg <= 72:
        return 'B-'
    elif 67 <= avg and avg <= 69:
        return 'C+'
    elif 63 <= avg and avg <= 66:
        return 'C'
    elif 60 <= avg and avg <= 62:
        return 'C-'
    elif 57 <= avg and avg <= 59:
        return 'D+'
    elif 53 <= avg and avg <= 56:
        return 'D'
    elif 50 <= avg and avg <= 52:
        return 'D-'
    elif avg >= 0 and avg <= 49:
        return 'F'

print(colours.bg.blue+"Welcome to the FIRST ever Math Quiz Application")#welcome message in blue highlight
print("You are going to get to test your integer facts!"+colours.reset)

questions = inputInteger("\nHow many random questions would you like to practise? ")#prompts user for number of question

counter = 1
total = 0
average = 0 

while counter <= questions: #commences loop
    choices = random.randint(1,4)
    operation_selected = operation(choices)#establishes operation in string form
    colour_of_question = questionColour(operation_selected) # gets the questions colour
    
    
    first_number = random.randint(-10,10) #gets the first and second numbers random integer values
    second_number = random.randint(-10, 10)
    
    expression = (colour_of_question+"\nQuestion #"+str(counter) + " of " + str(questions)+ ": "+str(first_number) +" " +str(operation_selected)+ " "+ str(second_number)+colours.reset) #makes the expression containing all the details
    print(expression) # prints the expression/question
    
    #checks the operation and then it calculates the answer and stores it in the integer variable answer
    if choices == 1: 
        answer = first_number + second_number
    elif choices == 2:
        answer = first_number - second_number
    elif choices == 3:
        answer = first_number * second_number
    else:
        answer = round(first_number / second_number, 2)
        print(colours.fg.lightcyan + "Round to 2 decimal places :)" + colours.reset)
    
    #asks user for their guess and makes sure that it is an input guess for the add, sub and multi questions and float guess for the div questions
    if operation_selected == '/':
        userAnswer = inputFloat("What is your guess? ")
    else:
        userAnswer = inputInteger("What is your guess? ")

    #checks if their answer is correct

    if userAnswer == answer: #answer is correct
        print(colours.fg.green+"You got it! Woo hoo!"+colours.reset)#prints green congrats message
        total += 100 # adds 100 to total
    else: #answer is incorrect
        print(colours.fg.red+"Sorry you got it wrong."+colours.reset)#prints red message saying that the answer is wrong and then in blue what the answer was
        print(colours.fg.blue+"The answer was ... "+str(answer)+colours.reset)
        total += 0 #adds 0 to the score

    average = round(total/counter, 2) #calculates new average
    print(colours.bg.green+"\t\tCurrent average is",str(average)+colours.reset+"\n") #prints the users current average in green highlight
    counter += 1 #adds 1 to the counter which represents the amount of questions
print("\n\nYour average on the integer quiz was:", str(average)+"%") #finally outputs the total average the user had on the quiz
letter = grade(average) #calculates the letter grade useing grade function
print("Your letter grade is:", letter ) #prints the users grade
print("Goodbye thank-you for using the integer quiz program !")#end message



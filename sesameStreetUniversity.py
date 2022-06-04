# This is the Sesame Street University program. It asks the user for information regarding their courses and grades and then outputs a formatted transcript. The program is programmed in a way to handle any errors or invalid inputs on its own without termination.
# Made for ICS3U1-03, by Arnav Dalmia
# class used: colours   This class was created by Emidio DiAntonio for ICS3U1-03, it allows the usage of colours in programs when used
# import random allows for the program to randomize numbers within parameters 

# functions
    # gradePoint()  This function will return the letter equivalence to a number grade inputted
    # isInteger()   This function will return True if a string is an integer or False if not
    # inputInteger()    This function will call the isInteger function to verify if a user's input is an integer. It will continue to ask the user for a valid integer input and then it will return the integer input
    # inputIntegerLow()     This function will call the inputInteger function and verify if the users inputted integer is lower than the low bound value. If it is then it will print an error and loop until a valid input is entered. After which the valid integer will be returned
    # inputIntegerBetween()    This function will call the inputInteger function and verify if the users inputted integer is between a lower bound and higher bound value. If it does not meet the requirments then the user will be returned a error message informing them that the value is either too high or low and will tell them the number requirments. It will repeat until a valid integer is entered
    # studentNumberFunction()   This function will create a randomized student number between 100000 and 500000
    # isMember()    This function will check if a target is in a list and return True or False if it is/isn't
    # enterCourse()     This function will ask the user for a course. It then calls the isMember function to verify that it is a valid course. If it isnt then it will show all the courses and then ask the user again. In the end the valid course is returned.
    # formatting()  This function will create the formatted  transcript  with all the data that  is accumulated throughout the process. It will then print said transcript
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

# inputIntegerLow(message, lowBound)
# message   This string variable contains the message that will be asked of the user
# lowBound   This integer variable represents the low bound of the user's integer input, it ensures that the user's input fits the requirement
# invalidInput  This boolean variable is used to verify if a input is a valid integer variable. Until invalidInput = False, then the loop will continue to ask for a valid integer 
# result    This variable contains the result of the user's input to message

# gradePoint(number)
# number    This integer variable contains a percentage grade that is converted into a letter grade

# studentNumberFunction()
# newNumber     This integer variable contains the randomized number between 100000-500000.

# isMember(myList, target)
# myList    This list function contains a list, in this case it shall be a list of courses that are offered at Sesame Street University
# target    This string variable contains a target that is checked if it is contained in myList
# found     This boolean variable contains the status if target is found in myList. False if not found, and True if found
# position  This integer variable is used to go between all the objects within myList

# enterCourse(message)
# message   This string variable contains the message that is asked of the user     
# condition     This boolean variable is used to loop the process of asking the users message. It is used to make sure that the input is valid
# chosenCourse      This string variable contains the users input in regarding the course
# *** listOfCourses IS NOT A LOCAL VARIABLE     

#formatting(name, number, listOfCourses, listOfGrades)
# name  This string variable contains the students name     
# number    This integer variable contains the student number of said student
# listOfCourses     This list contains the list of courses that the student has took
# listOfGrades      This list contains the list of grades to the courses that the student took
# line1     This string variable contains the first line of the Transcript. It has been formatted to contain different values
# line2     This string varialbe contains the second line of the Transcript. It has been formatted to contain different values
# line3     This string varialbe contains the third line of the Transcript. It has been formatted to contain different values
# line4     This string varialbe contains the fourth line of the Transcript. It has been formatted to contain different values
# line5     This string varialbe contains the fifth line of the Transcript. It has been formatted to contain different values
# line      This string varialbe contains the individual lines of the different courses formatted to have their name, grade and letter grade
# letter    This string variable contains the gradePoint return value which is the letter grade 
# average   This integer variable contains the percentage average of the student including all grades/courses 

# --------------------------- MAIN -----------------------------

import random # importing random for usage of student number 

def gradePoint(number):
    if number < 50: #checks the value of number
        return "F"# returns appropriate letter grade 
    elif number < 53:
        return "D-" 
    elif number < 57:
        return "D"
    elif number < 60:
        return "D+"
    elif number < 63:
        return "C-"
    elif number < 67:
        return "C"
    elif number < 70:
        return "C+"
    elif number < 73:
        return "B-"
    elif number < 77:
        return "B"
    elif number < 80:
        return "B+"
    elif number < 85:
        return "A-"
    elif number < 90:
        return "A"
    elif number >= 90:
        return "A+"
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
            print("Please enter a valid integer value")#outputs error message
    return result 
def inputIntegerLow(message,lowBound):#This function will call the inputInteger function and verify if the users inputted integer is lower than the low bound value. If it is then it will print an error and loop until a valid input is entered. After which the valid integer will be returned
    invalidInput = True # sets the boolean to false to loop
    while invalidInput:
        result = inputInteger(message) # asks users input
        if result < lowBound: #checks if it is above the lowBound
            print("Please enter a value larger than or equal to",lowBound) # error message printed if it is lower
        else: 
            invalidInput = False # ends loop if there are no problems
    return result # returns validated result
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
    return result
def studentNumberFunction():
    newNumber = random.randint(100000,500000)# generates random number between 100000-500000
    return newNumber # returns the number 
def isMember(myList,target): # this function will return True or False depending if target is found within myList
    found = False #sets base condition that target hasnt been found yet, so False
    position = 0 #sets to 0 to iterate through list
    while position < len(myList) and not found: #loops through myList to find target
        if myList[position] == target: #if target is found
            found = True# changes found to True
        position +=1
    
    return found# returns the end result either True or False
def enterCourse(message):#this function will ask the user for a course and verify if that course exists
    condition = False#sets to loop using boolean
    while not condition:#begin loop
        chosenCourse = input(message)#asks user for course
        
        if not isMember(listOfCourses, chosenCourse):#checks if the user chosenCourse is in the listOfCourses, if it isnt then it will say invalid course specified and it will show  all the vlaid courses
            print("Invalid Course Specified. Be sure to specify one of:")
            for i in listOfCourses:
                print("\t" + i)
            print("\n")
        else:
            condition = True #changes condition to True if the chosenCourse is found 
    return chosenCourse # after verifying that chosenCourse is valid it will return the string of the chosenCourse
def formatting(name, number,  listOfCourses, listOfGrades):    
    print("-"*85)#creates line of dashes
    line1 = "{0:<26} {1:>58}".format("Official School Transcript", "Sesame Streeet University")#title 
    print(line1)
    print("-"*85)#seperates using dashes
    
    line2 = "{0:<13} {1}".format("Student Name:", name)#line containing student name 
    line3 = "{0:<13} {1}".format( "Student Number:", number)# line containing student number
    
    print(line2)# prints name and student number
    print(line3)
    print("-"*85)#seperates using dashes
    
    line4 = "{0:<25} {1:^29} {2:>28}".format("Course Title", "Course Grade", "Corresponding Letter Grade")# header for grades and courses
    print(line4) # prints line
    for i in range(len(listOfGrades)): # prints all grades and courses in individual lines
        letter  = gradePoint(listOfGrades[i])
        line = "{0:<25} {1:^29} {2:^28}".format(listOfCourses[i], listOfGrades[i], letter)#makes lines for each course
        print(line)
        
    average = 0 #establishes average to be 0
    for i in listOfGrades:
        average += i
    average = average / len(listOfGrades)#Calculates average 
    
    print("\n")
    line5 = "{0:<13} {1}%".format("Student Overall Average: ",round(average, 2) )#line containing overall average
    print(line5)#prints line
    print("-"*85)#seperates using dashes
    print("End Of Transcript")#prints ending    
    print("-"*85)# seperates using dashes
    
# creates listOfCourses, these are the courses offered by 
listOfCourses = ["Literature", "Poetry", "Calculus", "Linear Algebra", "Chemistry", "Biology", "Basket Weaving", "Underwater Fire Prevention", "World History", "World Geography", "Canadian History", "Canadian Geography", "Economics", "French", "Spanish", "Italian"]

StudentsName = input("Please enter student's full name: ")#asks for students name
StudentNumber = studentNumberFunction() # Calculates students student number
numberOfGrades = inputIntegerLow("How many grades will you be entering: ", 1)# asks the users for how many grades they will be entering with a minimum of 1
courses = [""]*numberOfGrades # creates empty list of grades and courses
grades = [""]*numberOfGrades
for i in range(numberOfGrades):#loops through for number of courses from numberOfGrades
    enteredCourseName = enterCourse("Please enter course number #"+ str(i+1)+ ": ")# asks for course name using enterCourse funciton 
    grade = inputIntegerBetween("Please enter the grade for "+ enteredCourseName+ ": ", 0, 100) #asks for grade for said course
    courses[i] = enteredCourseName #adds the grade and course name to their respective lists
    grades[i] = grade
    
formatting(StudentsName, StudentNumber, courses, grades) # displays Transcript from formatting function




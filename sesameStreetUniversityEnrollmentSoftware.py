# CPT project of Arnav Dalmia. Made for ICS-3UI, for Emidio DiAntonio.
# Program title: Sesame Street University Enrollment software 
# Program description: This program will be the official Enrollment software of SSU. This program allows the teacher MR. COOKIES to create student account, and allow for the student to enroll into their courses. The teacher also has the ability to create a table containing the head count of how many people enrolled into each course
#
#
# Functions:
    # isInteger()   This function will return True if a string is an integer or False if not
    # inputInteger()    This function will call the isInteger function to verify if a user's input is an integer. It will continue to ask the user for a valid integer input and then it will return the integer input
    # inputIntegerBetween()    This function will call the inputInteger function and verify if the users inputted integer is between a lower bound and higher bound value. If it does not meet the requirments then the user will be returned a error message informing them that the value is either too high or low and will tell them the number requirments. It will repeat until a valid integer is entered
    # searchList()      This function will return a integer value of an index of the target string in a list
    # isMember()    This function will check if a target is in a list and return True or False if it is/isn't
    # deleteMemberUsingIndex()      This function will take 2 parameters,a list and a target index integer. The function will return the list with the exception of a value that is the indexed value of the list
    # enterCourse()     This function will ask the user for a course. It then calls the isMember function to verify that it is a valid course. If it isnt then it will show all the courses and then ask the user again. In the end the valid course is returned.
    # formatting()      This function will output a formatted table that contains the course count of each course. It will include official heading, and a list of the students that have enrolled in any courses. 
    # teacherOptions()      This function will first ask the user for their teacher credentials. It will verify the credentials and then proceed to asking what the teachers would like to do. They have 2 options which are to add student accounts or to create the formatted course count sheet.
    # logInStudent()        This function will verify a students log-in using their username and their student number
    # studentOptions()      This function will be in charge of asking the student for how many courses they want to enroll into. After the student has selected their courses, then they are informed that no more changes can be made.

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

# searchList(myList, target)
# myList    This list variable contains a list
# target    This string variable colntains the target of the list. It is what is checked for existing in the list
# i         This iterable variable represents the different cases of i between 0 and the length of the string. Used for checking if the target is found

# deleteMemberUsingIndex(myList, indexedTarget):
# myList        Previous and original list
# indexedTarget         The indexed value on myList that is gotten rid of. The new list excluding the indexedTarget is returned
# i         This iterable variable represents the index's of a list, myList. It is used for checking if it is the equivalent to the indexedTarget

# formatting(countOfEachCourse, individuals):
# countOfEachCourse     This list contains the count for each course
# individuals   This string contains a string with all the names of every student that has enrolled into a class
# line1     This string contains the first string that is the header
# line2     This string contains the line containing all the names of the students
# line3     This string contains the line with the headers of the courses and count
# line      This string is looped to syphen through every course, it is printed 15 times for every course
# listOfCourses, NOT A LOCAL VARIABLE, contains all 15 valid courses

# teacherOptions(listOfUserNames, listOfStudentNumbers):
# listOfUserNames   This list contains the list of all usernames for students
# listOfStudentNumbers      This list contains the list of all student numbers for students
# teacherLogIn      This boolean variable is used to verify if the teacher has logged in with the correct credentials
# usernameTeacher       This string variable contains the user inputted username for the teacher
# passwordTeacher       This string variable contains the user inputted pass for the teacher
# teacherOptionsBoolean         This boolean variable is used to loop through the teacher menu 
# optionChosenInTeacherOptions      This integer variable contains the user choice for the menu option, which has 3 options: 1,2,3
# studentsNameToBeAdded         This string variable contains the newly created students username, to be added to the listOfUserNames
# studentStudentNumberToBeAdded     This integer variable contains the newly created student number, to be added to the listOfStudentNumbers 


# logInStudent():
# verifiedLogin     This boolean variable is used to loop through the login process until the student has ssuccessfully logged in
# username      This string variable contains the students name, inputted
# studentNumber     This integer variable contains the students student number, inputted
# positionForNumber     This integer variable contains the index of the studentNumber in the list validStudentNumber
# positionForName       THis integer variable contains the index of the username in the list validUserName
# validUserName     NOT LOCAL, list containing the list of student's names
# validStudentNumber    NOT LOCAL, list containing the list of student numbers

# studentOptions(courses):
# courses       This list contains the list of courses that the student enrolls into, all compiled together
# numberOfCourses   This integer value is the user inputted value of the number of courses that the student wants to enrol into. Min of 1, max of 8
# condition     This boolean variable is used to loop through the process of asking for a unique course each time. Ensures that only one occurence of each course is enrolled into
# enteredCourseName     This string variable contains the name of indivual courses that are enrolled into


# --------------------------- MAIN PART 1 ---------------------------

# creates the full listOfCourses, with all 15 courses 
# creates empty lists of validUserName and validStudentNumber, to be added into later on
# assigns the Teacher's credentials using teacherName and teacherPassword
#
listOfCourses = ["Literature", "Poetry", "Calculus", "Linear Algebra", "Chemistry", "Biology", "Basket Weaving", "Underwater Fire Prevention", "World History", "World Geography", "Canadian History", "Canadian Geography", "Economics", "French", "Spanish", "Italian"]
validUserName = []
validStudentNumber = []
teacherName = "Cookie Monster" # teacher login
teacherPassword = "cookies"# teacher login


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
            print("Please enter a valid integer value")#outputs error message in red highlight
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
def searchList(myList,target): # this function will return True or False depending if target is found within myList
    for i in range(len(myList)):
        if myList[i] == target:
            return i 
def isMember(myList,target): # this function will return True or False depending if target is found within myList
    found = False #sets base condition that target hasnt been found yet, so False
    position = 0 #sets to 0 to iterate through list
    while position < len(myList) and not found: #loops through myList to find target
        if myList[position] == target: #if target is found
            found = True# changes found to True
        position +=1
    
    return found# returns the end result either True or False
def deleteMemberUsingIndex(myList, indexedTarget): #This function will take 2 parameters,myList and indexedTarget. The function will return the list with the exception of a value that is the indexed value of the list
    newList = []
    for i in range(len(myList)):
        if i != indexedTarget:
            newList += [myList[i]] # adds values that are not the same as indexedTarget
    return newList # returns the adjusted list
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
    return chosenCourse
def formatting(countOfEachCourse, individuals):    
    print("-"*85)#creates line of dashes
    line1 = "{0:<26} {1:>58}".format("Official Course-Count 2022", "Sesame Streeet University")#title 
    print(line1)
    print("-"*85)#seperates using dashes
    
    line2 = "{0:<13} {1}".format("Student Names:",individuals )#line containing students names 

    print(line2)# prints names
    print("-"*85)#seperates using dashes
    
    line3 = "{0:<25} {1:>29}".format("Course Title", "Enrollment Count")# header for title and amount
    print(line3 + "\n") # prints line
    for i in range(len(listOfCourses)): # prints all courses in individual lines
        line = "{0:<25} {1:>29}".format(listOfCourses[i], countOfEachCourse[i])#makes lines for each course
        print(line)
    print("-"*85)#creates line of dashes
    print("")
def teacherOptions(listOfUserNames, listOfStudentNumbers):
    print("\nPlease enter teacher LOG IN\n")
    teacherLogIn = False
    while not teacherLogIn: # loop for login
        usernameTeacher = input("Enter Teacher username: ") # user input ussername
        passwordTeacher = input("Enter password: ") # user input passowrd
        
        if (usernameTeacher == teacherName) and (passwordTeacher == teacherPassword):
            teacherLogIn = True  # checks if the teachers login credentials are valid, and if they are then the loop will terminate
        else:
            print("Invalid log in") # error message if log in fails
            
    print("\nWelcome Mr. Monster") # welcome message for teacher
    
    teacherOptionsBoolean = False #loop conditional boolean
    while not teacherOptionsBoolean:
        print("Teacher Options:\n\t1. Add Student\n\t2. Print Student Schedule\n\t3. Go Back To Previous Menu")#asks the user for their menu option between 1 and 3
        optionChosenInTeacherOptions = inputIntegerBetween("Please select a menu option: ", 1, 3) # stores choice in optionChosenInTeacherOptions
        if optionChosenInTeacherOptions == 1: #situation 1: adding a student
            studentsNameToBeAdded = input("Enter Student Name: ") # asks for studnet name
            studentStudentNumberToBeAdded = inputInteger("Enter Student Number: ") # asks for student number
            
            listOfUserNames += [studentsNameToBeAdded] # adds name to the listOfUserNames
            listOfStudentNumbers += [studentStudentNumberToBeAdded]# adds student number to listOfStudentNumbers
            
            print("Student Added\n")#prints confirmatory message, goes back to teacher menu
            
        elif optionChosenInTeacherOptions == 2: # situation 2: printing the formatted course count table
            stringOfNames = ""#creates empty string
            for i in namesOfStudentsThatHaveEnrolledInCourses:
                stringOfNames += i + ", "#adds every student that added courses to the stringOfNames
            
            formatting(courseCount, stringOfNames)#creates table 
            # goes back to teacher options menu

        else: # situation 3: leaving the teacher menu
            print("")
            teacherOptionsBoolean = True # ends the loop escaping the function
def logInStudent():
    
    print("\nPlease LOG IN") 
    
    verifiedLogin = False
    while not verifiedLogin: #commences loop
        username = input("Please enter your username: ") # asks for username
        studentNumber = inputInteger("Please enter your student number: ") # asks for student number
        
        if isMember(validStudentNumber, studentNumber) and isMember(validUserName, username): #verifies that the username and the student number exist
            positionForNumber = 0
            for i in range(len(validStudentNumber)):
                if validStudentNumber[i] == studentNumber:
                    positionForNumber = i # checks for the index  of the studentNumber and stores the value under positionForNumber
            positionForName = 0
            for i in range(len(validUserName)):
                if validUserName[i] == username:
                    positionForName = i  # checks for the index of the username and stores the value undre positionForName
                
            if positionForName == positionForNumber: # checks if both index's are the same, which indicates that they correspond to each other
                verifiedLogin = True    #ends loop if all is checked
                return username #in the end returns the username
            else:
                print("LOG IN FAILED. PLEASE TRY AGAIN")
        else:
            print("LOG IN FAILED. PLEASE TRY AGAIN")# if there are any problms then there will be an error message
def studentOptions(courses):
    
    print("Welcome\n") #welcome messagee
    print("Keep in mind, after you have selected your courses, they will be submitted. If there are any mistakes, ask the teacher to recreate your account and re-enter your courses\n") # prints a disclaimer indicating that after they are complete with this process their account will be deleted
    numberOfCourses = inputIntegerBetween("How many courses would you like to enrol into? ", 1, 8) # asks for how many courses they want to enroll into
    for i in range(numberOfCourses):
        condition = False 
        while not condition:
            #uses enterCourse function to get valid courses,        
            enteredCourseName = enterCourse("Please enter course number #"+ str(i+1)+ ": ")# asks for course name using enterCourse funciton
                    
            if isMember(courses, enteredCourseName) == True:
                print("You cannot enrol into a course more than once") #ensures that the student hasnt already enrolled into the same course
            else:
                condition = True  # after all things have been checked, the courses list is added with each course
        courses += [enteredCourseName] 
    return courses # returns the filled in list of enrolled in courses

# --------------------------- MAIN PART 2 ---------------------------



print("Welcome to the Sesame Street University Enrollment Software") # prints welcome message and basic rules
print("This software is a propriety software created by Head of Computer Science at SSU, Cookie Monster PhD\n*** If there are any problems with your account or the software make sure to consult Mr. Monster ***")
print("Ensure that your student account has been created by a teacher\n")



quit = False #commences loop, uses quit varaiable to make sure loop doesnt terminate until quit's value is changed 
courseCount = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] # establishes that 0 courses have been enrolled into so far, will be changed as progresment occurs
namesOfStudentsThatHaveEnrolledInCourses = [] # establishes empty list of students that enroll into courses

while not quit: # loop begin
    print("Sesame Street University Enrollment Software Options: \n\t1) Teacher\n\t2) Student\n\t3) Quit Program")#provides options
    option = inputIntegerBetween("Please select a menu option: ", 1, 3)#asks for users choice
    if option == 1: # if the choice is teacher, provides teacher options
        teacherOptions(validUserName, validStudentNumber) # uses function teacherOptions to provide options
    elif option == 2: # if the choice is student, provides student options 
        StudentsCourses = [] # creates empty list of courses that will be added to with function studentOptions
        name = logInStudent() # calls logInStudent function to allow the student login, the username will be returned and saved into the variable name
        StudentsCourses = studentOptions(StudentsCourses) # saves the return of studentOptions into StudentsCourses, which is a list
        

        print("You have successfully enrolled for your courses. You will no longer be able to make any changes")
        print("You have enrolled into: ") # shows the courses that were enrolled into
        for i in StudentsCourses:
            print("\t" + i)
        print("\n")
        
        indexOfPerson = searchList(validUserName, name) # finds index of username in the validUserName
        validUserName = deleteMemberUsingIndex(validUserName, indexOfPerson)
        validStudentNumber = deleteMemberUsingIndex(validStudentNumber, indexOfPerson) # deletes the student from the validUserName and validStudentNumber
        namesOfStudentsThatHaveEnrolledInCourses += [name] # adds the name of the student to namesOfStudentsThatHaveEnrolledInCourses list
        
        for i in StudentsCourses: # iterates through StudentsCourses and adds to the courseCount
            indexToBeAdded = searchList(listOfCourses, i)
            courseCount[indexToBeAdded] += 1 
    else:
        quit = True #ends loop if 3 is inputted, any other values wouldnt pass the option variable as there would be an error for any value that is greater than 3 or lower than 1

print("\nThank you for using the Sesame Street University Enrollment Software.") #end message




#Importing module
import webbrowser
import os

#Intro message
print("Hello and welcome to LoganBerry phone repair services\nPlease answer 'yes' or 'no' to the following questions\n")

#Defining variables
lineNumber = 0
yesTypes = ("yes", "yea", "y", "yep", "aye", "true")
noTypes = ("no", "nah", "n", "nope")
questionFileList = []
solutionFileList = []

#Defining exit sequence:
def exitSequence():
    enterToExit = input("Press enter to exit the program")
    os._exit(0)

#Opening files
try:
    questionFile = open("question file.txt", "r")
    solutionFile = open("solution file.txt", "r")

#Terminating the program if file not found error (run time error) is found
except FileNotFoundError:
    print("ERROR: The LoganBerry phone repair service is unable to open due to 1 or more missing text files\n")

    #Terminating the program
    exitSequence()

#Putting files into lists
for lines in questionFile:
    questionFileList.append(lines)
for lines in solutionFile:
    solutionFileList.append(lines)

#Starting main loop
while lineNumber < 11:

    #Asking question
    print("SYSTEM: ", questionFileList[lineNumber], "\n")

    #Accepting answer
    userInputCaseSensitive = input("USER: ")
    #Converting answer to lower case
    userInput = userInputCaseSensitive.lower()

    #Dealing with yes answers
    if userInput in yesTypes:
        lineNumber += 1
        print(solutionFileList[lineNumber -1], "\n")

        #Checking if user has fixed phone or not
        print("Is your problem resolved?\n")

        #Accepting answer
        userInputCaseSensitive = input("USER: ")
        #Converting answer to lower case
        userInput = userInputCaseSensitive.lower()

        #If problem is solved
        if userInput in yesTypes:
            #Exit message
            print("Thank you for using our phone repair program\n")

            #Terminating the program
            exitSequence()

        #If problem is not solved
        elif userInput in noTypes:
            pass
            
    #Dealing with no answers
    elif userInput in noTypes:
        lineNumber += 1
        print("Your answer has been recorded as no\n")

    #Dealing with invalid answers
    else:
        print("Invalid answer, please try again\n")

#Redirecting to phone repair site
webbrowser.open("http://www.gomobile.co.uk/help/repairs")

#Exit message
print("Thank you for using our phone repair program\n")

#Terminating the program
exitSequence()

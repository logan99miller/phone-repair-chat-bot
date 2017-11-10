#Importing module
import os

#Intro message
print("Hello and welcome to LoganBerry phone repair services\nPlease tell us what is wrong with your phone\n")

#Defining variables
yesTypes = ("yes", "yea", "y", "yep", "aye", "true")
noTypes = ("no", "nah", "n", "nope")
keyWordFileList = []
solutionFileList = []

#Defining exit sequence:
def exitSequence():
    enterToExit = input("Press enter to exit the program")
    os._exit(0)

#Opening files
try:
    keyWordFile = open("key word file.txt", "r")
    solutionFile = open("solution file.txt", "r")

#Terminating the program if file not found error (run time error) is found
except FileNotFoundError:
    print("ERROR: The LoganBerry phone repair service is unable to open due to 1 or more missing text files\n")

    #Terminating the program
    exitSequence()

#Putting files into lists
for lines in keyWordFile:
    keyWordFileList.append(lines.strip())
for lines in solutionFile:
    solutionFileList.append(lines)

#Starting main loop
while True:
    
    #Accepting problem
    userInputCaseSensitive = input("USER: ")
    #Converting answer to lower case
    userInput = userInputCaseSensitive.lower()

    #Repeating answer check 10 times
    for repeats in range(10):

        #Split up the keywords
        for values in keyWordFileList[repeats].split(","):

            #Displaying solution if keyword is found
            if values in userInput:
                print(solutionFileList[repeats], "\n")

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
                    break

                else:
                    pass
 
            else:
                pass

    #Repeating instructions if user's input was blank
    if userInput == "":
        print("Please tell us what is wrong with your phone\n")
            
    #Displaying message saying we cannot solve problem if the user's input was not blank
    else:
        print(solutionFileList[10], "\n")

pass

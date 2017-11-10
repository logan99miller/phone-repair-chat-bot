#Importing external modules
import os, webbrowser, winsound

def startUp():
    
    #Setting global variables
    global audioDict, yesTypes, noTypes, keyWordFileList, solutionFileList, iosDevice, androidDevice, windowsDevice, devices
    
    #Defining variables
    yesTypes = ("yes", "yea", "y", "yep", "aye", "true")
    noTypes = ("no", "nah", "n", "nope", "false")
    audioDict = {}
    keyWordFileList = []
    solutionFileList = []
    iosDevice = ["ios", "apple","iphone", "ipad", "ipod"]
    androidDevice = ["android", "samsung", "google", "nexus", "pixel"]
    windowsDevice = ["windows", "microsoft", "nokia", "lumia", "zune"]
    devices = [iosDevice, androidDevice, windowsDevice]

    #Trying to open audio files
    try:

        #Repeat process for each audio file
        for fileNumber in range(10):

            #Add android audio files to dictionary
            audioDict["android{0}".format(fileNumber)] = "audio/android" + str(fileNumber)

            #Add iOS audio files to dictionary
            audioDict["ios{0}".format(fileNumber)] = "audio/ios" + str(fileNumber)

            #Add windows audio files to dictionary
            audioDict["windows{0}".format(fileNumber)] = "audio/windows" + str(fileNumber)

        #Repeat process for each audio file
        for fileNumber in range(12):

            #Add generic audio files to dictionary
            audioDict["generic{0}".format(fileNumber)] = "audio/generic" + str(fileNumber)

    #Terminating the program if FileNotFoundError (a run time error) is found
    except FileNotFoundError:

        #Displaying exit message
        print("ERROR: The LoganBerry phone repair service is unable to open due to 1 or more missing files\n")
        #Playing above message
        winsound.PlaySound(audioDict.get("generic0"),winsound.SND_FILENAME)


        #Running exitSequence
        exitSequence()
   

    #Displaying intro message
    print("Hello and welcome to LoganBerry phone repair services, please note we only support devices running iOS, Android or Windows\n")
    #Playing above message
    winsound.PlaySound(audioDict.get("generic1"),winsound.SND_FILENAME)

def exitSequence():

    #Setting global variables
    global audioDict

    #Allowing user to choose to exit
    print("Press enter to exit the program\n")
    #Playing above message
    winsound.PlaySound(audioDict.get("generic2"),winsound.SND_FILENAME)

    enterToExit = input()
    

    #Exiting program
    os._exit(0)

def yesOrNoExit():

    #Setting global variables
    global audioDict, yesTypes, noTypes

    #Starting yes or no loop
    while True:

        #Accepting answer
        userInputCaseSensitive = input("USER: ")
            
        #Converting answer to lower case
        userInput = userInputCaseSensitive.lower()

        #If the user wants to exit
        if userInput in yesTypes:

            #Displaying exit message
            print("Thank you for using our phone repair program\n")
            #Playing above message
            winsound.PlaySound(audioDict.get("generic3"),winsound.SND_FILENAME)
                
            #Running exitSequence
            exitSequence()
                
        #Else, if the user wants to try again
        elif userInput in noTypes:

            #Exiting function
            return

        #Else yes or no answer not recognised
        else:
            
            print("Answer not recognised, please answer either yes or no\n")
            #Playing above message
            winsound.PlaySound(audioDict.get("generic4"),winsound.SND_FILENAME)

def device():

    #Setting global variables
    global audioDict, iosDevice, androidDevice, windowsDevice, devices, deviceModel, operatingSystem

    #Asking for device model
    print("Please tell us your device name/model (e.g. 'iPhone 5C 16GB Blue')\n")
    #Playing above message
    winsound.PlaySound(audioDict.get("generic5"),winsound.SND_FILENAME)

    #Accepting answer and storing answer under variable, deviceModel
    deviceModel = input("DEVICE NAME/MODEL: ")

    #Starting main device loop
    while True:

        #Asking for operating system
        print("Please tell us what operating system your phone has (either iOS, Android or Windows)\n")
        #Playing above message
        winsound.PlaySound(audioDict.get("generic6"),winsound.SND_FILENAME)

        #Accepting answer
        userInputCaseSensitive = input("USER: ")
        
        #Converting answer to lower case
        userInput = userInputCaseSensitive.lower()

        #Repeating process 3 times for the 3 operating systems / device types
        for deviceType in range(3):

            #Repeating process 5 times for the 5 key words linked to each operating system / device type
            for keyWord in range(5):

                #If the user's input equals the list in the devices list that corresponds with the deviceType integer and the string in the devices[deviceType] list that corresponds with the keyWord integer 
                if userInput == ((devices[deviceType])[keyWord]):

                    #Define operatingSystem as the string that corresponds with the integer 0, which is found in the list that corresponds with the deviceType integer in the devices list
                    operatingSystem = ((devices[deviceType])[0])

                    #Exiting function
                    return

        #Inform user that their input did not match any keywords and asking if they want to exit
        print("Operating system not supported or recognised, would you like to exit the program (if you answer no we will allow you to re-type / re-phrase your previous answer)?\n")
        #Playing above message
        winsound.PlaySound(audioDict.get("generic7"),winsound.SND_FILENAME)

        #Running yesOrNoExit
        yesOrNoExit()

def managingFiles():

    #Setting global variables
    global audioDict, keyWordFileList, solutionFileList, operatingSystem

    #Trying to open files in read mode
    try:
        
        keyWordFile = open("key word file.txt", "r")

        #Opening solution file specific to one chosen by user
        solutionFile = open(operatingSystem + " solution file.txt", "r")


    #Terminating the program if FileNotFoundError (a run time error) is found
    except FileNotFoundError:

        #Displaying exit message
        print("ERROR: The LoganBerry phone repair service is unable to open due to 1 or more missing files\n")
        #Playing above message
        winsound.PlaySound(audioDict.get("generic0"),winsound.SND_FILENAME)

        #Running exitSequence
        exitSequence()

    #Putting each line of the file as a separate item into a list
    for lines in keyWordFile:
        
        #.strip() used to remove the '\n' used to indicate a new line
        keyWordFileList.append(lines.strip())

    #Putting each line of the file as a separate item into a list 
    for lines in solutionFile:
        
        solutionFileList.append(lines)

def diagnosingProblem():

    #Setting global variables
    global audioDict, keyWordFileList, solutionFileList, operatingSystem, userInput

    #Displaying instructions
    print("Please tell us what is wrong with your", operatingSystem, "phone\n")
    #Playing above message
    winsound.PlaySound(audioDict.get("generic8"),winsound.SND_FILENAME)

    #Accepting problem
    userInputCaseSensitive = input("USER: ")

    #Converting answer to lower case
    userInput = userInputCaseSensitive.lower()

    #Repeating process 10 times for 10 problems program can diagnose
    for repeats in range(10):

        #Repeating process for each key word (separated by a comma) in the keyWordFileList that corresponds with the integer repeats
        for keyWords in keyWordFileList[repeats].split(","):

            #If a key word is found
            if keyWords in userInput:
                    
                #Displaying solution the corresponds with the integer repeats (and with the key word found)
                print(solutionFileList[repeats], "\n")

                #Playing above message
                if operatingSystem == "android":
                    winsound.PlaySound(audioDict.get("android" + str(repeats)),winsound.SND_FILENAME)
                elif operatingSystem == "ios":
                    winsound.PlaySound(audioDict.get("ios" + str(repeats)),winsound.SND_FILENAME)
                elif operatingSystem == "windows":
                    winsound.PlaySound(audioDict.get("windows" + str(repeats)),winsound.SND_FILENAME)

                #Checking if the user has resolved the problem
                print("Is your problem resolved?\n")
                #Playing above message
                winsound.PlaySound(audioDict.get("generic9"),winsound.SND_FILENAME)

                #Running yesOrNoExit
                yesOrNoExit()

                #Exiting function
                return
                
    #Display message
    print("Sorry, your problem was not recognised\n")
    #Playing above message
    winsound.PlaySound(audioDict.get("generic10"),winsound.SND_FILENAME)

    #Exiting function
    return

def diagnosticFailed():

    #Setting global variables
    global audioDict, solutionFileList, deviceModel, operatingSystem, userInput

    #Trying to assign this case the next case number in the cases.txt file
    try:
        
        #Defines caseNumber as integer of amount of lines in cases.txt
        caseNumber = len(open("cases.txt").readlines())

    #Creating a case file (using write mode) if FileNotFoundError (a run time error) is found
    except FileNotFoundError:

        cases = open("cases.txt", "w")

        #Closing case file so it can be used in a different mode
        cases.close()

        #Defines caseNumber as 0
        caseNumber = 0

    #Opening case file in appending mode
    cases = open("cases.txt", "a")

    #Appending case details to file
    cases.write("CASE NUMBER: " + str(caseNumber) + " | DEVICE TYPE: " + operatingSystem + " | DEVICE MODEL:" + deviceModel + " | USER'S PROBLEM: "  + userInput + "\n")

    #Closing case file
    cases.close()

    #Telling user they have a case number and we are googling the problem for them
    print("You have been assigned case number " + str(caseNumber) + ". A technician will be with you shortly\nWe will also show you google results related to your problem.")
    #Playing above message
    winsound.PlaySound(audioDict.get("generic11"),winsound.SND_FILENAME)

    #Opening manipulated Google URL containing key information about phone problem
    webbrowser.open("https://google.com/?q=" + operatingSystem + "+" + deviceModel + "+" + userInput)
    
    #Running exitSequence
    exitSequence()

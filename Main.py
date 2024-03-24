import sys
import Modules.Functions
#Initialize variables
userInput = ""
Condition = ""
#print main menu
Modules.Functions.Main_Menu()
# Getting Option
userInput = input("\nEnter your option to continue: ")
userInput = userInput.upper()
while userInput != "ESC":
    if (userInput == "AID"):
        Modules.Functions.AID()
    elif (userInput == "DID"):
        Modules.Functions.DID()
    elif (userInput == "UID"):
        Modules.Functions.UID()
    elif (userInput == "VID"):
        Modules.Functions.VID()
    elif (userInput == "SID"):
        Modules.Functions.SID()
    elif (userInput == "SDD"):
        Modules.Functions.SDD()
    elif (userInput == "VRL"):
        Modules.Functions.VRL()
    elif (userInput == "LDI"):
        Modules.Functions.LDI()
    else:
        print("\tWrong input, PLease enter again\t")
    userInput = input("\nEnter your option to continue: ")
    userInput = userInput.upper()
else:
    exit()




from collections import defaultdict
from loadPython import *
from printPython import printObjects
from summaryPython import showSummary
from detailsPython import showDetails
from provideHelp import showHelp
from savePython import saveObjects
from toset import toSet

validArgument = ["LOAD", "TOSET", "SAVE", "PRINT", "SUMMARY", "DETAILS", "QUIT"]
shapes = defaultdict(list)

badAnswer = True
load_performed = False  # Flag to track if the load operation has been performed
print("\033[1mWelcome,please pick one of the following operations:\033[0m")
print("\u2022 LOAD <<FILE>>")
print("\u2022 TOSET")
print("\u2022 SAVE")
print("\u2022 PRINT")
print("\u2022 SUMMARY")
print("\u2022 DETAILS")
print("\u2022 QUIT")
while badAnswer:
    userInput = input("Please enter the operation you would like to carry: ")
    wordsInUserInput=userInput.split()
    operation=userInput.split()[0]
    if operation.lower() == "load":
        if(len(wordsInUserInput)==1):
            print("you need to provide the name of the file you wish to load!")
            continue
        fileName=userInput.split()[1]
        print("Performing LOAD operation")
        shapes = loadObjects(fileName)
        load_performed = True
    elif operation.lower() == "save":
        if(len(wordsInUserInput)==1):
            print("you need to provide the name of the file you wish in to save in!")
            continue
        if not load_performed:
            print("No data is present to work on. Please load a file first.")
            continue
        savedFile = userInput.split()[1]
        print("Performing SAVE operation")
        if not load_performed:
            print("No data is present to work on. Please load a file first.")
            continue
        saveObjects(savedFile, shapes)
    elif operation.lower() == "summary":
        if not load_performed:
            print("No data is present to work on. Please load a file first.")
            continue
        print("Performing SUMMARY operation")
        showSummary(shapes)
    elif operation.lower() == "details":
        if not load_performed:
            print("No data is present to work on. Please load a file first.")
            continue
        print("Performing DETAILS operation")
        showDetails(shapes)
    elif operation.lower() == "print":
        if not load_performed:
            print("No data is present to work on. Please load a file first.")
            continue
        print("Performing PRINT operation")
        printObjects(shapes)
    elif operation.lower() == "toset":
        if not load_performed:
            print("No data is present to work on. Please load a file first.")
            continue
        print("Performing TOSET operation")
        toSet(shapes)
        print("duplicates have been removed successfully!")
    elif operation.lower() == "quit":
        print("Performing QUIT operation")
        print("Thank you for using our program \u2764\ufe0f")
        badAnswer = False
    else:
        print(operation, "is not a valid argument. Valid arguments are", validArgument)

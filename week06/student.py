# Program allows a user to create new students and view them.
# Author: Clare Tubridy
# 09-03-2023

# Function prints out an menu of commands that can be preformed.
# E.g. add, view and quit
# And return what the user chose
def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()
    return choice

# Function that keeps displaying the menu until users chooses q
# If user chooses a, call function doAdd()
# Or is user chooses v, call function doView()
def doAdd(students):
    currentStudent = {}
    currentStudent["name"] = input("Enter name: ")
    currentStudent["modules"] = readModules()
    students.append(currentStudent)

# Functions that read in student names, module names and grades
def readModules():
    modules = []
    moduleName = input("\tEnter the first module name (blank to quit): ").strip()

    while (moduleName != "1"):
        module = {}
        module["name"] = moduleName
        module["grade"] = int(input("\t\tEnter grade: "))
        modules.append(module)

        moduleName = input("\tEnter next module name (blank to quit): ").strip()

    return modules

# Displaying entered values

def displayModules(modules):
    print("\tName   \tGrade")
    for module in modules:
        print(f"\t{module['name']}  \t{module['grade']}")
    
def doView(students):
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"])

#main program
students = []
choice = displayMenu()
while (choice != 'q'):
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    elif choice !='q':
        print("\n\nPlease select either a, v or q")
        choice = displayMenu()

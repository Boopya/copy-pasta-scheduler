import os

def viewChoiceInputError():
    os.system("CLS")
    print('If you have chosen View Projects/Schedule Projects,')
    print('please combine the number choice with the letter choice.')
    print('\n\nExample: 2a - will view one project\n\n''')

def viewInvalidIdError():
    print("Please input a valid ID.\n\n")

def viewInvalidSizeError():
    print("Please input a valid number of pages.\n\n")

def viewInvalidTitleError():
    print("Please input the title of the project.\n\n")

def viewInvalidPriorityError():
    print("Please input a valid priority.\n\n")

def viewExistingIdError():
    os.system("CLS")
    print("Project with the same ID already exists.\nProject will not be added.\n\n")  
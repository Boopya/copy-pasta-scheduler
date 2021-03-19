import os

def viewConfirmInputDetails(id, title, size, priority):
    os.system("CLS")
    print("Confirm adding this Project?\n")
    print("\tProject ID: {}\n\tProject Title: {}\n\tNumber of pages: {}\n\tPriority: {}".format(id, title, size, priority))

def viewPoppedProject(id):
    os.system("CLS")
    print("Project with an ID number of {} has been added to completed projects.\n\n".format(id))      
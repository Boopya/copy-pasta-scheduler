import os
import csv

# Input Validation methods
def isValidNumber(num):
    try:
        num = int(num)
    except ValueError:
        return False
    else:
        return True

def isValidTitle(title):
    return len(title) != 0

def isUniqueId(project_id):
    try:
        with open('projects.txt', 'r') as csv_file:
            projects = csv.reader(csv_file)
            next(projects)
            for row in projects:
                if(row[0] == project_id):
                    return False
        return True
    # Returns a boolean value "False" if projects.txt is not yet created 
    except FileNotFoundError:
        os.system("CLS")
        print("You haven't input any projects yet.\n\n")
        return False
    except StopIteration:
        return True
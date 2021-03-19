import csv
import os
from project import Project

class ProjectController:
    __instance = None
    project_queue = []

    # Implemented as Singleton
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(ProjectController, cls).__new__(cls)
        return cls.__instance

    # Input Project methods
    def inputProject(self):
        with open('projects.txt', 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)

            # If projects.txt is empty, add header
            if(os.stat("projects.txt").st_size == 0):
                header = ['id', 'title', 'size', 'priority']
                writer.writerow(header)

            id = input("Project ID: ")
            title = input("Project Title: ")
            size = input("Number of pages: ")
            priority = input("Priority [1 - 10]: ")

            project = [id, title, size, priority]
            writer.writerow(project)
        
        os.system("CLS")
        print("Project added.\n\n")
            
    # View Projects methods
    def getOneProject(self, project_id):
        try:
            one_row = []

            with open('projects.txt', 'r') as csv_file:
                projects = csv.reader(csv_file)
                next(projects)
                for row in projects:
                    if(row[0] == project_id):
                        one_row = row
        # Returns a boolean value "False" if projects.txt is not yet created 
        except FileNotFoundError:
            os.system("CLS")
            print("You haven't input any projects yet.\n\n")
            return False
        # returns a list
        else:
            return one_row

    def getCompletedProjects(self):
        try:
            completed_projects = []

            with open('completed_projects.txt', 'r') as csv_file:
                projects = csv.reader(csv_file)
                next(projects)
                for row in projects:
                    completed_projects.append(row)
        # Returns a boolean value "False" if completed_projects.txt is not yet created
        except FileNotFoundError:
            os.system("CLS")
            print("You haven't completed any projects yet.\n\n")
            return False
        # returns a list
        else:
            return(completed_projects)

    def getAllProjects(self):
        try:
            all_projects = []

            with open('projects.txt', 'r') as csv_file:
                projects = csv.reader(csv_file)
                next(projects)
                for row in projects:
                    all_projects.append(row)
        # Returns a boolean value "False" if projects.txt is not yet created
        except FileNotFoundError:
            os.system("CLS")
            print("You haven't input any projects yet.\n\n")
            return False
        # returns a list
        else:
            return all_projects

    # Schedule Projects methods
    def createSchedule(self):
        try:
            project_queue = []

            with open('projects.txt', 'r') as source, open('schedule.txt', 'w', newline='') as dest:
                projects = csv.reader(source)
                schedule = csv.writer(dest)

                next(projects)
                for row in projects:
                    # Structure: [Priority, Size, ID, Title]
                    temp = [int(row[3]), int(row[2]), int(row[0]), row[1]]
                    project_queue.append(temp)

                project_queue.sort()
                ProjectController.project_queue = project_queue
                schedule.writerows(project_queue)
            
            os.system("CLS")
            print("Schedule created. You can now view updated schedule.\n\n")
        except FileNotFoundError:
            os.system("CLS")
            print("Please input project first.\n\n")

    # Get a Project method
    def getAProject(self):
        try:
            completed_projects = open('completed_projects.txt', 'r')
        except FileNotFoundError:
            os.system("CLS")
            print("Please create first a schedule.\n\n")
        else:  
            with open('completed_projects.txt', 'a') as completed_projects:
                project = ','.join(ProjectController.project_queue.pop(0))
                completed_projects.write(project + '\n')
                
            print('Project removed from the queue.')
            print(ProjectController.project_queue)
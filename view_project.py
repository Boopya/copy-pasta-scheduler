import csv
import os

class ViewProject:
    def viewMenu(self):
        print('1. Input Project Details')
        print('2. View Projects')
        print('\ta. One Project')
        print('\tb. Completed Projects')
        print('\tc. All Projects')
        print('3. Schedule Projects')
        print('\ta. Create Schedule')
        print('\tb. View Schedule')
        print('4. Get a Project')
        print('5. Exit')

    def viewOneProject(self, project):
        print(project)

    def viewCompletedProject(self, projects):
        print(projects)

    def viewAllProjects(self, projects):
        print(projects)

    def viewUpdatedSchedule(self):
        try:
            file_object = open('schedule.txt', 'r')
            projects = csv.reader(file_object)

            next(projects)
            for row in projects:
                print(row)
            
        except FileNotFoundError:
            os.system("CLS")
            print("Please create first a schedule.\n\n")
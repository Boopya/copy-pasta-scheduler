import csv
import os

class ViewProject:
    def viewMenu(self):
        os.system("CLS")

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
        # completed_projects.txt is not empty
        if not not projects:
            os.system("CLS")
            print(projects)
        else:
            os.system("CLS")
            print("There's nothing here.\n\n")

    def viewAllProjects(self, projects):
        # projects.txt is not empty
        if not not projects:
            os.system("CLS")
            print(projects)
        else:
            os.system("CLS")
            print("There's nothing here.\n\n")

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

    def viewChoiceInputError(self):
        os.system("CLS")
        print('If you have chosen View Projects/Schedule Projects,')
        print('please combine the number choice with the letter choice')
        print('\n\nExample: 2a - will view one project\n\n''')
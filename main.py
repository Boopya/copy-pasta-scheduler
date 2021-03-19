import os
from project_controller import ProjectController

def viewMenu():
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

controller = ProjectController()

schedule_queue = []

while True:
    viewMenu()
    choice = input('\nEnter your choice: ')

    if choice == '1':
        controller.inputProject()
    elif choice == '2':
        controller.viewChoiceInputError()
    elif choice == '2a':
        os.system("CLS")
        while True:
            id = input("Search by ID: ")
            # Invalid ID input
            if not controller.isValidNumber(id):
                controller.viewInvalidIdError()
            else:
                project = controller.getOneProject(id)
                controller.viewOneProject(project)
                break
    elif choice == '2b':
        projects = controller.getCompletedProjects()
        controller.viewCompletedProject(projects)
    elif choice == '2c':
        project = controller.getAllProjects()
        controller.viewAllProjects(project)
    elif choice == '3':
        controller.viewChoiceInputError()
    elif choice == '3a':
        controller.createSchedule()
    elif choice == '3b':
        controller.viewUpdatedSchedule()
    elif choice == '4':
        controller.getAProject()
    elif choice == '5':
        break
    else:
        os.system("CLS")
        print("Invalid input.\n\n")

    os.system("PAUSE")
    os.system("CLS")
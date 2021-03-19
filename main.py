import os
from project_controller import ProjectController
from view_project import ViewProject

controller = ProjectController()
viewer = ViewProject()

schedule_queue = []

while True:
    viewer.viewMenu()
    choice = input('\nEnter your choice: ')

    if choice == '1':
        controller.inputProject()
    elif choice == '2':
        viewer.viewChoiceInputError()
    elif choice == '2a':
        os.system("CLS")
        while True:
            id = input("Search by ID: ")
            # Invalid ID input
            if not controller.isValidNumber(id):
                viewer.viewInvalidIdError()
            else:
                project = controller.getOneProject(id)
                # project returns a list instead of a False value
                if project is not False:
                    viewer.viewOneProject(project)
                break
    elif choice == '2b':
        project = controller.getCompletedProjects()
        # project returns a list instead of a False value
        if project is not False:
            viewer.viewCompletedProject(project)
    elif choice == '2c':
        project = controller.getAllProjects()
        # project returns a list instead of a False value
        if project is not False:
            viewer.viewAllProjects(project)
    elif choice == '3':
        viewer.viewChoiceInputError()
    elif choice == '3a':
        controller.createSchedule()
    elif choice == '3b':
        viewer.viewUpdatedSchedule()
    elif choice == '4':
        controller.getAProject()
    elif choice == '5':
        break
    else:
        os.system("CLS")
        print("Invalid input.\n\n")

    os.system("PAUSE")
    os.system("CLS")
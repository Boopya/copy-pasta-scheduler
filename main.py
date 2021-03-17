import os
from project_controller import ProjectController
from view_project import ViewProject

controller = ProjectController()
viewer = ViewProject()

schedule_queue = []

while True:
    viewer.viewMenu()
    choice = input('Enter your choice: ')

    if choice == '1':
        controller.inputProject()
    elif choice == '2a':
        os.system("CLS")
        id = input("\nSearch by ID: ")
        project = controller.getOneProject(id)
        viewer.viewOneProject(project)
    elif choice == '2b':
        project = controller.getCompletedProjects()
        viewer.viewCompletedProject(project)
    elif choice == '2c':
        project = controller.getAllProjects()
        viewer.viewAllProjects(project)
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
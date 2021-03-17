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
        schedule_queue = controller.createSchedule()
    elif choice == '3b':
        if(controller.schedule_created is True):
            viewer.viewUpdatedSchedule(schedule_queue)
        else:
            print("Please create first a schedule.")
    elif choice == '5':
        break
    else:
        break

    os.system("PAUSE")
    os.system("CLS")
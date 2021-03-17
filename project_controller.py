import csv
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

            id = input("Project ID: ")
            title = input("Project Title: ")
            size = input("Number of pages: ")
            priority = input("Priority [1 - 10]: ")

            project = [id, title, size, priority]
            writer.writerow(project)
            
    # View Projects methods
    def getOneProject(self, project_id):
        with open('projects.txt', 'r') as csv_file:
            projects = csv.reader(csv_file)
            next(projects)
            for row in projects:
                if(row[0] == project_id):
                    # print(row)
                    return(row)
    
    def getCompletedProjects(self):
        completed_projects = []

        with open('completed_projects.txt', 'r') as csv_file:
            projects = csv.reader(csv_file)
            next(projects)
            for row in projects:
                completed_projects.append(row)
        
        # print(completed_projects)
        return(completed_projects)

    def getAllProjects(self):
        all_projects = []

        with open('projects.txt', 'r') as csv_file:
            projects = csv.reader(csv_file)
            next(projects)
            for row in projects:
                all_projects.append(row)
        
        # print(all_projects)
        return(all_projects)

    # Schedule Projects methods
    def createSchedule(self):
        project_queue = []

        with open('projects.txt', 'r') as source, open('schedule.txt', 'w', newline='') as dest:
            projects = csv.reader(source)
            schedule = csv.writer(dest)

            next(projects)
            for row in projects:
                # Structure: [Priority, Size, ID] (for easy sorting)
                temp = [int(row[3]), int(row[2]), int(row[0]), row[1]]
                project_queue.append(temp)

            project_queue.sort()
            schedule.writerows(project_queue)
            
        print("Schedule created. You can now view updated schedule.")

    # Get a Project method
    def getAProject(self):
        print('Project removed from the queue.')
        with open('completed_projects.txt', 'a') as completed_projects:
            project = ','.join(ProjectController.project_queue.pop(0))
            completed_projects.write(project + '\n')

import csv

class ProjectController:   
    project_queue = [['69', 'Title 69', '69', '69']]

    # View Projects methods
    def getOneProject(self, project_id):
        with open('projects.txt', 'r') as csv_file:
            projects = csv.reader(csv_file)
            next(projects)
            for row in projects:
                if(row[0] == project_id):
                    print(row[0])
    
    def getCompletedProjects(self):
        completed_projects = []

        with open('completed_projects.txt', 'r') as csv_file:
            projects = csv.reader(csv_file)
            next(projects)
            for row in projects:
                completed_projects.append(row)
        
        print(completed_projects)

    def getAllProjects(self):
        all_projects = []

        with open('projects.txt', 'r') as csv_file:
            projects = csv.reader(csv_file)
            next(projects)
            for row in projects:
                all_projects.append(row)
        
        print(all_projects)

    # Schedule Projects methods
    def createSchedule(self):
        with open('projects.txt', 'r') as csv_file:
            projects = csv.reader(csv_file)
            next(projects)
            for row in projects:
                ProjectController.project_queue.append(row)
            

    def viewUpdatedSchedule(self):


    # Get a Project method
    def getAProject(self):
        print('Project removed from the queue.')
        with open('completed_projects.txt', 'a') as completed_projects:
            project = ','.join(ProjectController.project_queue.pop(0))
            completed_projects.write(project + '\n')
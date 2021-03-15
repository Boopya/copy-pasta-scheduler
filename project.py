import csv

class Project:

    def __init__(self, id, title, size, priority):
        self.id = id
        self.title = title
        self.size = size
        self.priority = priority
    
    def getTitle(self):
        return title
    
    def getSize(self):
        return size
    
    def getPriority(self):
        return priority

    def getOneProject(self, project_id):
        with open('projects.txt', 'r') as csv_file:
            projects = csv.reader(csv_file)
            next(projects)
            for row in projects:
                if(row[0] == project_id):
                    print(row[0])
    
    def getAllProjects(self):
        project_list = []
        
        with open('projects.txt', 'r') as csv_file:
            projects = csv.reader(csv_file)
            next(projects)
            for row in projects:
                project_list.append(row)
        
        print(project_list)

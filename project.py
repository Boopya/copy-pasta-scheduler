import csv

class Project:

    def __init__(self, id, title, size, priority):
        self.id = id
        self.title = title
        self.size = size
        self.priority = priority
    
    def getTitle():
        return title
    
    def getSize():
        return size
    
    def getPriority():
        return priority

    def getOneProject(self, id):
        with open('projects.txt', 'r') as csv_file:
            projects = csv.reader(csv_file)
            next(projects)
            for row in projects:
                if row[0] == id:
                    print(row[0])

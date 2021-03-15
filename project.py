import csv

class Project:
    def __init__(self, project_id, title, size, priority):
        self.id = project_id
        self.title = title
        self.size = size
        self.priority = priority
class ProjectController:   
    
    # Implement as Singleton

    def getOneProject(project_id):
        with open('projects.txt', 'r') as csv_file:
            projects = csv.reader(csv_file)
            next(projects)
            for row in projects:
                if(row[0] == project_id):
                    print(row[0])
    
    def getCompletedProjects():
        project_list = []

        with open('completed_projects.txt', 'r') as csv_file:
            projects = csv.reader(csv_file)
            next(projects)
            for row in projects:
                project_list.append(row)
        
        print(project_list)

    def getAllProjects():
        project_list = []

        with open('projects.txt', 'r') as csv_file:
            projects = csv.reader(csv_file)
            next(projects)
            for row in projects:
                project_list.append(row)
        
        print(project_list)

    def getAProject():
        # TODO
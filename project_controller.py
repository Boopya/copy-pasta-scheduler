import csv
import os
from project import Project
from view_project import ViewProject

class ProjectController:
    __instance = None
    project_queue = []
    viewer = ViewProject()

    # Class implemented as Singleton
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(ProjectController, cls).__new__(cls)
        return cls.__instance

    # Constructor
    def __init__(self):
        self.fetchData()

    # Method to initialize queue based on schedule.txt
    def fetchData(self):
        try:
            with open('schedule.txt', 'r') as csv_file:
                schedule = csv.reader(csv_file)
                
                next(schedule)
                for row in schedule:
                    ProjectController.project_queue.append(row)
        except(FileNotFoundError, StopIteration) as e:
            pass

    # Input Project method
    def inputProject(self):
        with open('projects.txt', 'a', newline='') as all_projects, open('pending_projects.txt', 'a', newline='') as pending_projects:
            all_writer = csv.writer(all_projects)
            pend_writer = csv.writer(pending_projects)

            # If projects.txt is empty, add header
            if(os.stat("projects.txt").st_size == 0):
                header = ['id', 'title', 'size', 'priority']
                all_writer.writerow(header)
                pend_writer.writerow(header)

            os.system("CLS")
            while True:
                # Input ID
                while True:
                    id = input("Project ID: ")
                    if not self.isValidNumber(id):
                        self.viewer.viewInvalidIdError()
                    else: break
                # Input Title
                while True:
                    title = input("Project Title: ")
                    if not self.isValidTitle(title):
                        self.viewer.viewInvalidTitleError()
                    else: break
                # Input Number of Pages
                while True:
                    size = input("Number of pages: ")
                    if not self.isValidNumber(size):
                        self.viewer.viewInvalidSizeError()
                    else: break
                # Input Priority
                while True:
                    priority = input("Priority [1 - 10]: ")
                    if not self.isValidNumber(priority) or int(priority) not in range(1, 11):
                        self.viewer.viewInvalidPriorityError()
                    else: break

                self.viewer.viewConfirmInputDetails(id, title, size, priority)
                choice = input("\nOptions:\n\t1 - Yes\n\tOther - No\n\nChoice: ")
                if choice == '1':
                    # Conflicting ID with another project
                    if not self.isUniqueId(id):
                        self.viewer.viewExistingIdError()
                    else:
                        project = [id, title, size, priority]
                        all_writer.writerow(project)
                        pend_writer.writerow(project)

                        os.system("CLS")
                        print("Project added.\n\n")
                else:
                    os.system("CLS")
                    print("Cancelled.\n\n")
                break
    
    # Input Validation methods
    def isValidNumber(self, num):
        try:
            num = int(num)
        except ValueError:
            return False
        else:
            return True

    def isValidTitle(self, title):
        return len(title) != 0

    def isUniqueId(self, project_id):
        try:
            with open('projects.txt', 'r') as csv_file:
                projects = csv.reader(csv_file)
                next(projects)
                for row in projects:
                    if(row[0] == project_id):
                        return False
            return True
        # Returns a boolean value "False" if projects.txt is not yet created 
        except FileNotFoundError:
            os.system("CLS")
            print("You haven't input any projects yet.\n\n")
            return False
        except StopIteration:
            return True
            
    # View Projects methods
    def getOneProject(self, project_id):
        try:
            one_row = []

            with open('projects.txt', 'r') as csv_file:
                projects = csv.reader(csv_file)
                next(projects)
                for row in projects:
                    if(row[0] == project_id):
                        one_row = row
        # Returns a boolean value "False" if projects.txt is not yet created 
        except FileNotFoundError:
            os.system("CLS")
            print("You haven't input any projects yet.\n\n")
            return False
        # returns a list
        else:
            return one_row

    def getCompletedProjects(self):
        try:
            completed_projects = []

            with open('completed_projects.txt', 'r') as csv_file:
                projects = csv.reader(csv_file)
                next(projects)
                for row in projects:
                    completed_projects.append(row)
        # Returns a boolean value "False" if completed_projects.txt is not yet created
        except FileNotFoundError:
            os.system("CLS")
            print("You haven't completed any projects yet.\n\n")
            return False
        # returns a list
        else:
            return(completed_projects)

    def getAllProjects(self):
        try:
            all_projects = []

            with open('projects.txt', 'r') as csv_file:
                projects = csv.reader(csv_file)
                next(projects)
                for row in projects:
                    all_projects.append(row)
        # Returns a boolean value "False" if projects.txt is not yet created
        except FileNotFoundError:
            os.system("CLS")
            print("You haven't input any projects yet.\n\n")
            return False
        # returns a list
        else:
            return all_projects

    # Schedule Projects methods
    def createSchedule(self):
        try:
            project_queue = []

            with open('pending_projects.txt', 'r') as source, open('schedule.txt', 'w', newline='') as dest:
                projects = csv.reader(source)
                schedule = csv.writer(dest)

                # If schedule.txt is empty, add header
                if(os.stat("schedule.txt").st_size == 0):
                    header = ['priority', 'size', 'id', 'title']
                    schedule.writerow(header)
                
                next(projects)
                for row in projects:
                    # Structure: [Priority, Size, ID, Title]
                    temp = [int(row[3]), int(row[2]), int(row[0]), row[1]]
                    project_queue.append(temp)

                project_queue.sort()
                ProjectController.project_queue = project_queue
                os.system("CLS")
                if len(project_queue) == 0:
                    print("You have no pending projects, thus scheduling is not available.\n\n")
                else:
                    schedule.writerows(project_queue)
                    print("Schedule created. You can now view schedule.\n\n")
        except FileNotFoundError:
            os.system("CLS")
            print("Please input project first.\n\n")

    # Get a Project method
    def getAProject(self):
        # Check if schedule.txt is already existing
        if len(ProjectController.project_queue) == 0:
            os.system("CLS")
            print("Please create first a schedule.\n\n")
        else:
            try:
                with open('completed_projects.txt', 'a', newline='') as complete:
                    comp_writer = csv.writer(complete)
                    """ 
                    Re-arrange the content of the project to be popped:
                    [0][0] - priority --> id
                    [0][1] - size --> title
                    [0][2] - id --> size
                    [0][3] - title --> priority
                    """
                    id = ProjectController.project_queue[0][2]
                    title = ProjectController.project_queue[0][3]
                    size = ProjectController.project_queue[0][1]
                    priority = ProjectController.project_queue[0][0]

                    completed = [id, title, size, priority]
                    self.viewer.viewPoppedProject(id)

                    # If completed_projects.txt is empty, add header
                    if(os.stat("completed_projects.txt").st_size == 0):
                        header = ['id', 'title', 'size', 'priority']
                        comp_writer.writerow(header)
                    
                    # Pop from queue then add to completed_projects.txt
                    ProjectController.project_queue.pop(0)
                    comp_writer.writerow(completed)

                    # Update pending_projects.txt
                    self.updatePendingProjects(id)
            except FileNotFoundError:
                os.system("CLS")
                print("Please create first a schedule.\n\n")

    # Method to update the pending_projects.txt
    def updatePendingProjects(self, id):
        temp_list = []

        id = str(id)
        # Read pending_projects.txt to prepare for write
        with open('pending_projects.txt', 'r') as source:
            reader = csv.reader(source)
            for row in reader:
                if row[0] == id:
                    continue
                else:
                    temp_list.append(row)

        with open('pending_projects.txt', 'w', newline='') as dest:
            writer = csv.writer(dest)
            writer.writerows(temp_list)

        # with open('pending_projects.txt', 'w') as dest:
        #     dest.writelines(temp_list)

        # with open('pending_projects.txt', 'r') as source, open('temp.txt', 'w', newline='') as dest:
        #     reader = csv.reader(source)
        #     writer = csv.writer(dest)
        #     for row in reader:
        #         if row[0] != id:
        #             writer.writerow(row)

        # with open('temp.txt', 'r') as source, open('pending_projects.txt', 'w', newline='') as dest:
        #     reader = csv.reader(source)
        #     writer = csv.writer(dest)
        #     for row in reader:
        #         if row[0] != id:
        #             writer.writerow(row)

        # os.remove('temp.txt')

            
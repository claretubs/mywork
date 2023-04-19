# Program that has 3 attributes that are set by an __init__ function
# Author: Clare Tubridy

class Timesheetentry:
    
    def __init__(self, project, start, duration):
        self.project = project
        self.start = start              # Datetime object
        self.duration = duration        # Minutes
    
    # Returns the project and duration
    def __str__(self):
        return self.project + ':' + str(self.duration)

# Test case for this class that creates an instance and prints it out
import datetime as dt

if __name__ == '__main__':
    ts = dt.datetime(2021,3,19,16,20)
    test = Timesheetentry('test', ts, 60)
    print(test)

# Author: Clare Tubridy

from timesheetentry import *

class Employee:
    timesheets = []

    def __init__(self, first, last):
        self.first = first
        self.last = last
        
    def __str__(self):
        return self.first + ' ' + self.last
    
    def logminutes(self, project, minutes):
        now = dt.datetime.now
        timesheetentry = Timesheetentry(project, now, minutes)
        self.timesheets.append(timesheetentry)
    
    def gettotaltime(self):
        total_minutes = 0
        for ts in self.timesheets:
            total_minutes += ts.duration
        return total_minutes
    

if __name__ == '__main__':
    test = Employee('Clare', 'Tubridy')
    print(test)
    assert('Clare Tubridy' == str(test))
    test.logminutes('p1', 30)
    test.logminutes('p1', 60)
    mins = test.gettotaltime()
    assert( mins == 90)
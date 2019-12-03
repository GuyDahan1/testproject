from TestClass import test
from QuestionClass import question
class course(test):
    def __init__(self, name, yr, sr):
        self.name_course = name
        self.year = yr
        self.semester = sr
        self.testList=[]
    def addTest(self,yr,seme,ddl):
        self.testList.append(test(yr,seme,ddl))
        print('Added new test')


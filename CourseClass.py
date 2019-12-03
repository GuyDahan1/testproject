from TestClass import test
class course:
    def __init__(self, name, tst, yr, sr):
        name_course = name
        test = tst
        year = yr
        semester = sr
    def addingTest(self,yr,seme,ddl):
        self.testList.append(yr,seme,ddl)
        print('Added new test')
    name_course = ""
    testList = []
    year = ""
    semester = ""

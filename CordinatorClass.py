from LecturerClass import lecturer
from CourseClass import course
from TestClass import test
class cordinator(lecturer):
    def newLecturer(self,nm,pl,proff,passw):
        """Creates and returns new lecturer"""
        return lecturer(nm,pl,proff,passw)
    def newCourse(self,name,year,semester):
        return course(name,year,semester)
    def newTest(self,yr,seme,ddl):
        return test(yr,seme,ddl)





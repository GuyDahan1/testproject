from LecturerClass import lecturer
from StudentClass import student
class coordinator:
    name_coordinator = ""
    phone_coordinator = ""
    profession_coordinator = ""
    password_coordinator = ""
    def __index__(self,nc,pc,proffc,passc):
        self.name_coordinator=nc
        self.password_coordinator=passc
        self.phone_coordinator=pc
        self.password_coordinator=passc
    def newLecturer(self,nm,pl,proff,passw):
        """Creates and returns new lecturer"""
        return lecturer(nm,pl,proff,passw)
    def newStudent(self,ns,ps,proffs,passs):
        """Creates new student"""
        return student(ns,ps,proffs,passs)

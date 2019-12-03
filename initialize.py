from CordinatorClass import cordinator
from LecturerClass import lecturer
from StudentClass import student
from CourseClass import course
from TestClass import test
from QuestionClass import question
def cordinatorCreate():
    """Function returns cordinator"""
    name=input("Enter Cordinator name\n")
    phone=input("Enter Phone number\n")
    proffesion=input("Enter proffesion\n")
    password=input("Enter Password\n")
    newCordinator=cordinator(name,phone,proffesion,password)
    return newCordinator
def lecturerCreate():
    """Function returns lecturer"""
    name=input("Enter Lecturer name\n")
    phone=input("Enter Phone number\n")
    proffesion=input("Enter proffesion\n")
    password=input("Enter Password\n")
    newLecturer=lecturer(name,phone,proffesion,password)
    return newLecturer
def studentCreate():
    """Function returns student"""
    name=input("Enter Student name\n")
    phone=input("Enter Phone number\n")
    proffesion=input("Enter proffesion\n")
    password=input("Enter Password\n")
    newStudent=student(name,phone,proffesion,password)
    return newStudent
def courseCreate():
    """Function returns course"""
    name=input("Enter Course name\n")
def printMenu():
    print("""Menu:
    1.Add new Crdinator
    2.Add new Lecturer
    3.Add new Student
    4.Add new Course
    5.Add new Test
    6.Add new Question""")
def starting():
    cordinatorList=[]
    lecturerList=[]
    studentList=[]
    courseList=[]
    testList=[]
    questionList=[]
    printMenu()
    flag=input()
    if flag==1:
        cordinatorList.append(cordinatorCreate())
    elif flag==2:
        lecturerList.append(lecturerCreate())
    elif flag==3:
        studentList.append(studentCreate())




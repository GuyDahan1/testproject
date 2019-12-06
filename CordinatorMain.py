from initialize import *
from Class.CordinatorClass import cordinator
from Class.LecturerClass import lecturer
from Class.StudentClass import student
from Class.CourseClass import course
from Class.TestClass import test
from Class.QuestionClass import question

def imp_cor(corlist):
    """Importing Cordinators"""
    cordi_file = open("Data\Cordinators.txt", 'r')
    for i in cordi_file:
        temp=i.split()
        corlist.append(cordinator(temp[0]+temp[1],temp[2],temp[3],temp[4]))
    cordi_file.close()
def imp_lecturers(leclist):
    lec_file=open("Data\Lecturers.txt",'r')
    for i in lec_file:
        temp=i.split()
        leclist.append(lecturer(temp[0] + temp[1], temp[2], temp[3], temp[4]))
    lec_file.close()
def imp_students(stdlist):
    std_file=open("Data\Students.txt",'r')
    for i in std_file:
        temp=i.split()
        stdlist.append(student(temp[0] + temp[1], temp[2], temp[3], temp[4]))
    std_file.close()
def imp_courses(courlist):
    course_file=open("Data\Courses.txt",'r')
    for i in course_file:
        temp=i.split()
        courlist.append(course(temp[0],temp[1],temp[2]))
    course_file.close()
def imp_q(qlist):
    q_file=open("Data\Students.txt",'r')
    for i in q_file:
        temp=i.split()
        qlist.append(question(course(temp[0],temp[1],temp[2]),test(temp[3],temp[4],temp[5]),temp[6],temp[7],temp[8],temp[9],temp[10],temp[11],temp[12]))
    q_file.close()



config_file=open("Config.txt",'r')
config_info=config_file.readline().split()
#0-initialized 1-Cordinator counter 2-Lecturer counter 3-Student counter 4-Courses counter 5-Question counter
config_file.close()
while config_info[0]=='0':
    starting()
    config_file = open("Config.txt", 'r')
    config_info = config_file.readline().split()
    config_file.close()
cordinatorList=[]
lecturerList=[]
studentList=[]
courseList=[]
testList=[]
questionList=[]
if config_info[1]!='0':
    imp_cor(cordinatorList)
    print("Imported Cordinators")
if config_info[2]!='0':
    imp_lecturers(lecturerList)
    print("Imported Lecturers")
if config_info[3]!='0':
    imp_students(studentList)
    print("Imported Students")
if config_info[4]!='0':
    imp_courses(courseList)
    print("Imported Courses")
if config_info[5]!='0':
    imp_q(questionList)
    print("Imported Questions")
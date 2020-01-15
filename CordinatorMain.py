from initialize import *
from Class.CordinatorClass import cordinator
from Class.LecturerClass import lecturer
from Class.StudentClass import student
from Class.CourseClass import course
from Class.TestClass import test
from Class.QuestionClass import question
#import PyPDF3



def imp_cor(corlist):
    """Importing Cordinators"""
    cordi_file = open("Data\Cordinators.txt", 'r')
    for i in cordi_file:
        temp = i.split()
        corlist.append(cordinator(temp[0] + ' ' + temp[1], temp[2], temp[3], temp[4]))
    cordi_file.close()


def imp_lecturers(leclist):
    """Importing Lecturer from txt file in the agreed format"""
    lec_file = open("Data\Lecturers.txt", 'r')
    for i in lec_file:
        temp = i.split()
        leclist.append(lecturer(temp[0] + ' ' + temp[1], temp[2], temp[3], temp[4]))
    lec_file.close()


def imp_students(stdlist):
    """Importing Students from txt file in the agreed format"""
    std_file = open("Data\Students.txt", 'r')
    for i in std_file:
        temp = i.split()
        stdlist.append(student(temp[0] + ' ' + temp[1], temp[2], temp[3], temp[4]))
    std_file.close()


def imp_courses(courlist):
    """Importing Courses from txt file in the agreed format"""
    course_file = open("Data\Courses.txt", 'r')
    for i in course_file:
        temp = i.split()
        courlist.append(course(temp[0], temp[1], temp[2]))
    course_file.close()


def imp_q(qlist):
    """Importing Questions from txt file in the agreed format"""
    q_file = open("Data\Questions.txt", 'r')
    for i in q_file:
        temp = i.split()
        difflist=[]
        for x in range(0,int(temp[13])):
            difflist.append(temp[14+x])
        qlist.append(
            question(course(temp[0], temp[1], temp[2]), test(temp[3], temp[4], temp[5],temp[12]), temp[6], temp[7], temp[8],
                     difflist, temp[9], temp[10], temp[11],temp[13])
        )
    q_file.close()


def print_cordinator_menu():
    """Printing current Menu"""
    print("""Cordinator Menu:
    1.Add new course
    2.Add new question to an existing course
    3.Update Cordinator info
    4.Update Lecturer info
    5.Update Student info
    6.New Cordinator
    7.New Lecturer
    8.New Student
    9.Save and Quit""")


def new_question_to_course(courseList):
    """Function will add a new question to an existing course"""
    flag1 = True
    while flag1:
        name = input("Enter course name\n")
        for x in courseList:
            if name == x.getName():
                newtest = testCreate(x)
                newQ=questionCreate(x, newtest)
                if newtest.is_cropped():
                    newtest.__crop__(newQ.getCode())
                    newQ.setPdf()
                return newQ
        print("Wrong course name\n")
        ff = input("To try again enter 1")
        if ff != '1':
            flag1 = False


def update_student_plus(studentList):
    """Function will recive a list (student\lecturer\cordinator)
    and will update the requested user password or phone"""
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO, filename='LOG.txt')#Writing to log file
    logging.info('Update_student initialized')#Writing to log file
    flag1 = True
    while flag1:
        name = input("Enter name\n")
        for x in studentList:
            if name == x.getName():
                flag2 = input("1.Change password\n2.Change phone")
                if flag2 == '1':
                    x.setPassword(input("Enter new password\n"))
                    logging.info(name + ' changed password')#Writing to log file
                    return
                elif flag2 == '2':
                    x.setPhone(input("Enter new phone\n"))
                    logging.info(name + ' changed phone')#Writing to log file
                    return
        flag3 = input("Name not found Try again?(1=Y)")
        if flag3 != '1':
            flag1 = False

############MAIN START###########
config_file = open("Config.txt", 'r')
config_info = config_file.readline().split()
# 0-initialized 1-Cordinator counter 2-Lecturer counter 3-Student counter 4-Courses counter 5-Question counter
config_file.close()
while config_info[0] == '0':
    print("hello user , This is your first entry")
    starting()
    config_file = open("Config.txt", 'r')
    config_info = config_file.readline().split()
    config_file.close()
cordinatorList = []
lecturerList = []
studentList = []
courseList = []
testList = []
questionList = []
if config_info[1] != '0':
    imp_cor(cordinatorList)
    print("Imported Cordinators")
if config_info[2] != '0':
    imp_lecturers(lecturerList)
    print("Imported Lecturers")
if config_info[3] != '0':
    imp_students(studentList)
    print("Imported Students")
if config_info[4] != '0':
    imp_courses(courseList)
    print("Imported Courses")
if config_info[5] != '0':
    imp_q(questionList)
    print("Imported Questions")
flag1 = True
while flag1:
    print_cordinator_menu()
    flag2 = input()
    if flag2 == '1':
        startup(courseList, testList, questionList)
    elif flag2 == '2':
        questionList.append(new_question_to_course(courseList))
    elif flag2 == '3':
        update_student_plus(cordinatorList)
    elif flag2 == '4':
        update_student_plus(lecturerList)
    elif flag2 == '5':
        update_student_plus(studentList)
    elif flag2 == '6':
        temp = user_create(1, cordinatorList)
        if temp:
            cordinatorList.append(temp)
    elif flag2 == '7':
        temp = user_create(2, lecturerList)
        if temp:
            lecturerList.append(temp)
    elif flag2 == '8':
        temp = user_create(3, studentList)
        if temp:
            studentList.append(temp)
    elif flag2 == '9':
        saveToFiles(cordinatorList, lecturerList, studentList, courseList, testList, questionList)
        flag1 = False

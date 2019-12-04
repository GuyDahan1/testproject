"""First startup of the database"""

from CordinatorClass import cordinator
from LecturerClass import lecturer
from StudentClass import student
from CourseClass import course
from TestClass import test
from QuestionClass import question
def cordinatorCreate():
    """Function returns new cordinator"""
    name=input("Enter Cordinator name\n")
    phone=input("Enter Phone number\n")
    proffesion=input("Enter proffesion\n")
    password=input("Enter Password\n")
    newCordinator=cordinator(name,phone,proffesion,password)
    return newCordinator
def lecturerCreate():
    """Function returns new lecturer"""
    name=input("Enter Lecturer name\n")
    phone=input("Enter Phone number\n")
    proffesion=input("Enter proffesion\n")
    password=input("Enter Password\n")
    newLecturer=lecturer(name,phone,proffesion,password)
    return newLecturer
def studentCreate():
    """Function returns new student"""
    name=input("Enter Student name\n")
    phone=input("Enter Phone number\n")
    proffesion=input("Enter proffesion\n")
    password=input("Enter Password\n")
    newStudent=student(name,phone,proffesion,password)
    return newStudent
def courseCreate():
    """Function returns new course"""
    name=input("Enter Course name\n")
    year=input("Enter Course year\n")
    semester=input("Enter Course semester\n")
    return course(name,year,semester)
def testCreate():
    """Function returns new test"""
    year=input("Enter Test year\n")
    semester=input("Enter Test semester\n")
    deadline=input("Enter Test deadline\n")
    return test(year,semester,deadline)
def questionCreate(course,test):
    """Function recives a course and test as parameters and returns new question"""
    question_code = input("Enter question code\n")
    main_topic = input("Enter main topic\n")
    sub_theme = input("Enter sub topic\n")
    difficulty = input("Enter difficulty\n")
    solution_type = input("Enter solution type\n")
    format = input("Enter question format\n")
    test_exams = input("Test/Exam\n")
    return question(course,test,question_code,main_topic,sub_theme,difficulty,solution_type,format,test_exams)

def startup(courseList,testList,questionList):
    """Function recives 3 lists Course,Test,Question and will initialize them"""
    flag1=True
    flag2=True
    flag3=True
    counter1=0
    counter2=0
    while flag1:
        print("Creating new Course")
        courseList.append(courseCreate())
        while flag2:
            print("Creating new Test")
            testList.append(testCreate())
            while flag3:
                print("Creating new questions")
                questionList.append(questionCreate(courseList[counter1],testList[counter2]))
                print("To add another question to this course and test enter 1")
                if input()!=1:
                    flag3=False
            counter2+=1
            print("To add another Test to this course enter 1")
            if input() != 1:
                flag2 = False
        counter1+=1
        print("To add another Course enter 1")
        if input() != 1:
            flag1 = False

def saveToFiles(cordinatorList,lecturerList,studentList,courseList,testList,questionList):
    """Function will save all info to files"""
    cordi_counter=0
    lectur_counter=0
    student_counter=0
    file_cordi = open("Cordinators.txt",'w')
    file_lectur = open("Lecturers.txt", 'w')
    file_student = open("Students.txt", 'w')
    for x in cordinatorList:
        file_cordi.write(str(x))
        cordi_counter+=1
    for x in lecturerList:
        file_lectur.write(str(x))
        lectur_counter+=1
    for x in studentList:
        file_student.write(str(x))
        student_counter+=1
    file_student.close()
    file_lectur.close()
    file_cordi.close()
    file_course=open("Courses.txt",'w')
    course_counter=0
    for x in courseList:
        file_course.write(str(x))
        course_counter+=1
    file_course.close()
    file_questions=open("Questions.txt",'w')
    question_counter=0
    for x in questionList:
        file_questions.write(str(x))
        question_counter+=1
    file_questions.close()
    file_config=open("Config.txt",'w')
    file_config.write("{0} {1} {2} {3} {4} {5}".format('1',cordi_counter,lectur_counter,student_counter,course_counter,question_counter))
    file_config.close()

def printMenu():
    print("""Menu:
    1.Add new Crdinator
    2.Add new Lecturer
    3.Add new Student
    4.Add new Course
    5.Save all
    6.Quit""")
def starting():
    cordinatorList=[]
    lecturerList=[]
    studentList=[]
    courseList=[]
    testList=[]
    questionList=[]
    flag2=True
    while flag2:
        printMenu()
        flag=int(input())
        if flag==1:
            cordinatorList.append(cordinatorCreate())
        elif flag==2:
            lecturerList.append(lecturerCreate())
        elif flag==3:
            studentList.append(studentCreate())
        elif flag==4:
            startup(courseList,testList,questionList)
        elif flag==5:
            saveToFiles(cordinatorList, lecturerList, studentList, courseList, testList, questionList)
        elif flag==6:
            flag2=False



starting()
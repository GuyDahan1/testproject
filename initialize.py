"""First startup of the database"""
import logging
import timeit
from Class.CordinatorClass import cordinator
from Class.LecturerClass import lecturer
from Class.StudentClass import student
from Class.CourseClass import course
from Class.TestClass import test
from Class.QuestionClass import question
import PyPDF3

#output = PyPDF3.PdfFileWriter()

def cordinatorCreate():
    """Function returns new cordinator"""
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO,filename='LOG.txt')
    logging.info('Cordinator_create initialized')
    start1=timeit.default_timer()
    name = input("Enter Cordinator name(Full name,First Last)\n")
    phone = input("Enter Phone number\n")
    proffesion = input("Enter proffesion\n")
    password = input("Enter Password\n")
    newCordinator = cordinator(name, phone, proffesion, password)
    stop1=timeit.default_timer()
    logging.info('Cordinator created ,Runtime='+"{0:.2f}".format(stop1-start1)+' Seconds')
    return newCordinator


def lecturerCreate():
    """Function returns new lecturer"""
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO, filename='LOG.txt')
    logging.info('Lecturer_create initialized')
    start1 = timeit.default_timer()
    name = input("Enter Lecturer name(Full name,First Last)\n")
    phone = input("Enter Phone number\n")
    proffesion = input("Enter proffesion\n")
    password = input("Enter Password\n")
    newLecturer = lecturer(name, phone, proffesion, password)
    stop1 = timeit.default_timer()
    logging.info('Lecturer created ,Runtime='+"{0:.2f}".format(stop1-start1)+' Seconds')
    return newLecturer


def studentCreate():
    """Function returns new student"""
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO, filename='LOG.txt')
    logging.info('student_create initialized')
    start1 = timeit.default_timer()
    name = input("Enter Student name(Full name,First Last)\n")
    phone = input("Enter Phone number\n")
    proffesion = input("Enter proffesion\n")
    password = input("Enter Password\n")
    newStudent = student(name, phone, proffesion, password)
    stop1 = timeit.default_timer()
    logging.info('Student created ,Runtime='+"{0:.2f}".format(stop1-start1)+' Seconds')
    return newStudent


def courseCreate():
    """Function returns new course"""
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO, filename='LOG.txt')
    logging.info('course_create initialized')
    start1 = timeit.default_timer()
    name = input("Enter Course name\n")
    while True:
        year = input("Enter Course year\n")
        if int(year) >=1990 & year <=2021:
            break
        else :
            print("Invalid year, valid year 1990-2021")
    semester = input("Enter Course semester\n")
    newcourse= course(name, year, semester)
    stop1 = timeit.default_timer()
    logging.info('Course created ,Runtime='+"{0:.2f}".format(stop1-start1)+' Seconds')
    return newcourse


def testCreate(course):
    """Function returns new test"""
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO, filename='LOG.txt')
    logging.info('test_create initialized')
    start1 = timeit.default_timer()
    year = course.year
    semester = course.semester
    deadline = input("Enter Test deadline\n")
    Path = input("please enter test.pdf Path\n")
    newtest= test(year, semester, deadline,Path)
    stop1 = timeit.default_timer()
    logging.info('test created ,Runtime='+"{0:.2f}".format(stop1-start1)+' Seconds')
    return newtest


def questionCreate(course, test):
    """Function recives a course and test as parameters and returns new question"""
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO, filename='LOG.txt')
    logging.info('question_create initialized')
    start1 = timeit.default_timer()
    question_code = input("Enter question code\n")
    main_topic = input("Enter main topic\n")
    sub_theme = input("Enter sub topic\n")
    sectionCount=input("Enter how many sections\n")
    difficulty=[]
    for i in range(0,int(sectionCount)):
        difficulty.append(input("Enter difficulty\n"))
    solution_type = input("Enter solution type\n")
    format = input("Enter question format\n")
    test_exams = input("Test/Exam\n")
    newquestion= question(course, test, question_code, main_topic, sub_theme, difficulty, solution_type, format, test_exams,sectionCount)
    stop1 = timeit.default_timer()
    logging.info('question_create initialized ,Runtime='+"{0:.2f}".format(stop1-start1)+' Seconds')
    return newquestion


def startup(courseList, testList, questionList):
    """Function recives 3 lists Course,Test,Question and will initialize them"""
    flag1 = True
    flag2 = True
    flag3 = True
    counter1 = 0
    counter2 = 0
    counter3=0
    while flag1:
        print("Creating new Course")
        courseList.append(courseCreate())
        while flag2:
            print("Creating new Test")
            testList.append(testCreate(courseList[counter1]))
            while flag3:
                print("Creating new questions")
                questionList.append(questionCreate(courseList[counter1], testList[counter2]))
                print("Cropping Question from test")
                testList[counter2].__crop__(questionList[counter3].getCode())
                questionList[counter3].setPdf()
                counter3+=1
                print("To add another question to this course and test enter 1")
                if input() != '1':
                    flag3 = False
            counter2 += 1
            print("To add another Test to this course enter 1")
            if input() != '1':
                flag2 = False
        counter1 += 1
        print("To add another Course enter 1")
        if input() != '1':
            flag1 = False


def saveToFiles(cordinatorList, lecturerList, studentList, courseList, testList, questionList):
    """Function will save all info to files"""
    cordi_counter=0
    lectur_counter=0
    student_counter=0
    file_cordi = open("Data\Cordinators.txt", 'a')
    file_lectur = open("Data\Lecturers.txt", 'a')
    file_student = open("Data\Students.txt", 'a')
    for x in cordinatorList:
        file_cordi.write(str(x) + '\n')
        cordi_counter += 1
    for x in lecturerList:
        file_lectur.write(str(x) + '\n')
        lectur_counter += 1
    for x in studentList:
        file_student.write(str(x) + '\n')
        student_counter += 1
    file_student.close()
    file_lectur.close()
    file_cordi.close()
    file_course=open("Data\Courses.txt",'w')
    course_counter=0
    file_course = open("Data\Courses.txt", 'a')
    course_counter = 0
    for x in courseList:
        file_course.write(str(x) + '\n')
        course_counter += 1
    file_course.close()
    file_questions=open("Data\Questions.txt",'w')
    question_counter=0
    file_questions = open("Data\Questions.txt", 'a')
    question_counter = 0
    for x in questionList:
        file_questions.write(str(x) + '\n')
        question_counter += 1
    file_questions.close()
    file_config = open("Config.txt", 'w')
    file_config.write(
        "{0} {1} {2} {3} {4} {5}".format('1', cordi_counter, lectur_counter, student_counter, course_counter,
                                         question_counter))
    file_config.close()


def printMenu():
    print("""Menu:
    1.Add new Crdinator
    2.Add new Lecturer
    3.Add new Student
    4.Add new Course
    5.Save and Quit""")


def starting():
    cordinatorList = []
    lecturerList = []
    studentList = []
    courseList = []
    testList = []
    questionList = []
    flag2 = True
    while flag2:
        printMenu()
        flag = input()
        if flag == '1':
            cordinatorList.append(cordinatorCreate())
        elif flag == '2':
            lecturerList.append(lecturerCreate())
        elif flag == '3':
            studentList.append(studentCreate())
        elif flag == '4':
            startup(courseList, testList, questionList)
        elif flag == '5':
            flag2 = False
            saveToFiles(cordinatorList, lecturerList, studentList, courseList, testList, questionList)
        else:
            print("invaild value")


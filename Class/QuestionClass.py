from Class.CourseClass import course
from Class.TestClass import test
import PyPDF2

class question:
    def __init__(self,course,test, qc, mt, st, dif, sult, Format, te , PDF):
        self.course=course
        self.test=test
        self.question_code = qc
        self.main_topic = mt
        self.sub_theme = st
        self.difficulty = dif
        self.solution_type = sult
        self.format = Format
        self.test_exams = te
        self.pdfFille = PDF

    def pdfToString(self):


    def __str__(self):
        return '{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12}'.format(self.course.name_course,self.course.year,self.course.semester,self.test.year,self.test.semester,self.test.deadline,self.question_code,self.main_topic,self.sub_theme,self.difficulty,self.solution_type,self.format,self.test_exams)

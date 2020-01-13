from Class.CourseClass import course
from Class.TestClass import test
import PyPDF3
#from pdf2image import *


class question:
    def __init__(self, course, test, qc, mt, st, dif, sult, Format, te,seccount):
        self.course = course
        self.test = test
        self.question_code = qc
        self.main_topic = mt
        self.sub_theme = st
        self.solution_type = sult
        self.format = Format
        self.test_exams = te
        self.section_diff_list=dif
        self.section_count=seccount
        self.difficulty=0
        for x in self.section_diff_list:
            self.difficulty+=int(x)
        self.path = "Class\pdfFileHere\{0}.pdf".format(qc)
        self.pdf=None
        self.image =None

    #def pdfToString(self):

    def getCode(self):
        return self.question_code
    def setPdf(self):
        self.pdf = PyPDF3.PdfFileReader(self.path, "rb")
        #self.image= pdf2image.convert_from_path(self.path)

    # def imageToWord(self):
    #    docs = docx.Document()
    #   parg = docs.add_paragraph()
    #  r = parg.add_run()
    # r.add_text('question number 1:\n')
    # r.add_picture('exemple.png')
    # docs.save('exe.docx')

    def __str__(self):
        str1='{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13}'.format(self.course.name_course,
                                                                             self.course.year,
                                                                             self.course.semester,
                                                                             self.test.year, self.test.semester,
                                                                             self.test.deadline,
                                                                             self.question_code, self.main_topic,
                                                                             self.sub_theme,
                                                                             self.solution_type, self.format,
                                                                             self.test_exams, self.path,self.section_count)
        for x in self.section_diff_list:
            str1=str1+' '+x
        return str1



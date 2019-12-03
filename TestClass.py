from QuestionClass import question
class test:
    def __init__(self,yr,seme,ddl):
        self.year=yr
        self.semester=seme
        self.deadline=ddl
        self.questionList=[]
    def addQuestion(self,qc, mt, st, dif, sult, yr, smes, dl, Format, te):
        """Adding new question to the list"""
        self.questionList.append(question(qc, mt, st, dif, sult, yr, smes, dl, Format, te))
        print('New question created')

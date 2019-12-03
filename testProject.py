#git gat

class question:
    def __init__(self, qc, mt, st, dif, sult, yr, smes, dl, Format, te):
        question_code = qc
        main_topic = mt
        sub_theme = st
        difficulty = dif
        solution_type = sult
        year = yr
        semester = smes
        deadline = dl
        format = Format
        test_exams = te

    question_code = ""
    main_topic = ""
    sub_theme = ""
    difficulty = ""
    solution_type = ""
    year = ""
    semester = ""
    deadline = ""
    format = ""
    test_exams = ""


class test:
    def __init__(self,yr,seme,ddl):
        self.year=yr
        self.semester=seme
        self.deadline=ddl
    def addQuestion(self,qc, mt, st, dif, sult, yr, smes, dl, Format, te):
        """Adding new question to the list"""
        self.questionList.append(question(qc, mt, st, dif, sult, yr, smes, dl, Format, te))
        print('New question created')
    questionList = []
    year = ""
    semester = ""
    deadline = ""


class course:
    def __init__(self, name, tst, yr, sr):
        name_course = name
        test = tst
        year = yr
        semester = sr
    def addingTest(self,yr,seme,ddl):
        self.testList.append(yr,seme,ddl)
        print('Added new test')
    name_course = ""
    testList = []
    year = ""
    semester = ""


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


class lecturer:
    def __init__(self,nl,pl,proffl,passl):
        self.name_lecturer=nl
        self.password_lecturer=pl
        self.profession_lecturer=proffl
        self.password_lecturer=passl

    name_lecturer = ""
    phone_lecturer = ""
    profession_lecturer = ""
    password_lecturer = ""


class student:
    def __init__(self,ns,ps,proffs,passs):
        self.name_student=ns
        self.password_student=passs
        self.phone_student=ps
        self.profession_student=proffs
    name_student = ""
    phone_student = ""
    profession_student = ""
    password_student = ""

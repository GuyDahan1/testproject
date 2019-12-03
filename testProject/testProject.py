

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

    name_course = ""
    testList = test("")
    year = ""
    semester = ""


class coordinator:
    name_coordinator = ""
    phone_coordinator = ""
    profession_coordinator = ""
    password_coordinator = ""


class lecturer:
    name_lecturer = ""
    phone_lecturer = ""
    profession_lecturer = ""
    password_lecturer = ""


class student:
    name_student = ""
    phone_student = ""
    profession_student = ""
    password_student = ""

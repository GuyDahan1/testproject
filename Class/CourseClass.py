class course():
    def __init__(self, name, yr, sr):
        self.name_course = name
        self.year = yr
        self.semester = sr
    def getName(self):
        return self.name_course
    def __str__(self):
        return "{0} {1} {2}".format(self.name_course,self.year,self.semester)

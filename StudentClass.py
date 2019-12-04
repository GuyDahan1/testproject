class student:
    def __init__(self,name,phone,proffs,passs):
        self.name=name
        self.password=passs
        self.phone=phone
        self.profession=proffs
    def __str__(self):
        return "{0} {1} {2} {3}".format(self.name,self.profession,self.phone,self.password)

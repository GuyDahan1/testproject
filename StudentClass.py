class student:
    def __init__(self,name,phone,proffs,passs):
        self.name=name
        self.password=passs
        self.phone=phone
        self.profession=proffs
    def changePassword(self,newpass):
        self.password=newpass
    def changePhone(self,newPhone):
        self.phone=newPhone

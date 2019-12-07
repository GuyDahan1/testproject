import PyPDF3


class test:
    def __init__(self, yr, seme, ddl, Path):
        self.year = yr
        self.semester = seme
        self.deadline = ddl
        """לעשות פה תנאי חבדוק עם הpath קיים שלא ישלח אותנו מהקובץ\\check the PATH!!!"""
        TestPdf = PyPDF3.PdfFileReader(Path, "rb")
        self.tPdf = TestPdf
        self.path=Path

    def getPdf(self):
        return self.tPdf
    def getPath(self):
        return self.path

    def __crop__(self):
        flag1=True
        while flag1:
            pagNum=int(input("Enter page number"))
            upperX = int(input("please enter upper x cordinate"))
            upperY = int(input("please enter upper y cordinate"))
            lowerX = int(input("please enter lower x cordinate"))
            lowerY = int(input("please enter lower y cordinate"))
            path = self.getPath()
            writer = PyPDF3.PdfFileWriter()
            page = self.tPdf.getPage(pagNum)
            page.cropBox.setLowerLeft((lowerX, lowerY))
            page.cropBox.setUpperRight((upperX, upperY))
            writer.addPage(page)
            name = input("Enter question code\n")
            path = "pdfFileHere\{0}.pdf".format(name)
            outstream = open(path, 'wb')
            writer.write((outstream))
            outstream.close()
            flag2=input("Enter 1 to crop another question\n")
            if flag2!='1':
                flag1=False


path=input("path\n")
test1=test('1992','b','b',path)
test1.__crop__()

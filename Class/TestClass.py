import PyPDF3
import pdf2image
import docx


class test:
    def __init__(self, yr, seme, ddl, Path):
        self.year = yr
        self.semester = seme
        self.deadline = ddl
        while True:
            try:
                TestPdf = PyPDF3.PdfFileReader(Path, "rb")
                break
            except:
                print("File not found")
                Path = input("Enter new path\n")
        self.tPdf = TestPdf
        self.path = Path
        #self.image = pdf2image.convert_from_path(Path)

    def getPdf(self):
        return self.tPdf

    def getPath(self):
        return self.path

    def __crop__(self,name):
        pagNum = int(input("Enter page number\n"))
        upperX = int(input("please enter upper x cordinate\n"))
        upperY = int(input("please enter upper y cordinate\n"))
        lowerX = int(input("please enter lower x cordinate\n"))
        lowerY = int(input("please enter lower y cordinate\n"))
        path = self.getPath()
        writer = PyPDF3.PdfFileWriter()
        page = self.tPdf.getPage(pagNum)
        page.cropBox.setLowerLeft((lowerX, lowerY))
        page.cropBox.setUpperRight((upperX, upperY))
        writer.addPage(page)
        path = "Class\pdfFileHere\{0}.pdf".format(name)
        outstream = open(path, 'wb')
        writer.write((outstream))
        outstream.close()



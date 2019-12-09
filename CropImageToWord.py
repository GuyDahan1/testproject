"""Function recives a path of an pdf file and inserts it in a Word File
--------Not Complete Code---------"""

from pdf2image import convert_from_path
from PyPDF2 import PdfFileReader,PdfFileWriter
from wand.image import Image

string=input()
with open(string+".pdf","rb") as in_f:
    input1=PdfFileReader(in_f)
    output1=PdfFileWriter()
    numPages=input1.getPage()
    for i in range(numPages):
        page=input1.getPage(i)
        print(page.mediaBox.getUpperRight_x(),page.mediaBox.getUpperRight_y())
        page.trimBox.lowerLeft=(25,25)
        page.trimBox.upperLeft=(225,225)
        page.cropBox.loweRight=(50,50)
        page.cropBox.upperRight=(200,200)
        output1.addPage(page)
    with open("PdfToImage.pdf","wb") as out_f:
        output1.write(out_f)
pages=convert_from_path('PdfToImage.pdf',500)
for page in pages:
    page.save('PdfToImage.jpg','JPEG')

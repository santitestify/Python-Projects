import PyPDF2

Pdf_File = open("example.pdf", "rb")  # rb for double code

PDF_Reader = PyPDF2.PdfFileReader(Pdf_File)

first_page = PDF_Reader.getPage(0).extractText()
second_page = PDF_Reader.getPage(1).extractText()
third_page = PDF_Reader.getPage(2).extractText()

print(first_page)
print(second_page)
print(third_page)






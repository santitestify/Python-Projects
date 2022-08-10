import PyPDF2
import pyttsx3

Engine = pyttsx3.init()
PDF_Reader = PyPDF2.PdfFileReader(open("example.pdf", "rb"))

for Page_num in range(PDF_Reader.numPages):
    text = PDF_Reader.getPage(Page_num).extractText()
    # Engine.say(text)
    # Engine.runAndWait()
    Engine.save_to_file(text, "audio.mp3")
    Engine.runAndWait()
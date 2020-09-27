import pyttsx3
import PyPDF2

book = open('D:\\Downloads\\Bernard Cornwell - The Grail Quest - 2 - Vagabond ( PDFDrive ).pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)  # gets the file to read
pages = pdfReader.numPages  # gets the number of the pages
speaker = pyttsx3.init()  # initialize speaker
newVoiceRate = 160  # voice rate
voices = speaker.getProperty('voices')  # get the property. In that case voices. It can be gender and age also

speaker.setProperty('voice', voices[0].id)  # set property
print("Name: " + voices[0].name)
volume = speaker.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
print("Volume: " + str(volume))  # printing current volume level
speaker.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1
speaker.setProperty('rate', newVoiceRate)  # setting up voice rate
print("Voice speed: " + str(newVoiceRate))  # printing current voice rate
print("Number of pages: " + str(pages))
for num in range(3, pages):
    page = pdfReader.getPage(num)
    print("Current page: " + str(num + 1))
    text = page.extractText()
    speaker.say(text)
    # speaker.save_to_file('Hello World', 'test.mp3') saves to a file
    speaker.runAndWait()
#  speaker.stop() is to stop the speaker engine

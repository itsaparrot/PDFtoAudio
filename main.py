from dotenv import load_dotenv
import PyPDF2
import os
import requests

load_dotenv()
my_text = ''

with open('PDF/sample.pdf', 'rb') as pdf_object:
    pdf_reader = PyPDF2.PdfFileReader(pdf_object)
    pages = pdf_reader.numPages
    # extracts text from each PDF page, assigns it to a string
    for i in range(0, pages):
        page_object = pdf_reader.getPage(i)
        my_text += page_object.extractText()

voicerss = os.environ.get('VOICERSS_API_KEY')
parameters = {
    'key': voicerss,
    'src': my_text,
    'hl': 'en-us',
    'v': 'Linda',
    'c': 'MP3',
}

response = requests.get("http://api.voicerss.org/", params=parameters)
response.raise_for_status()
audio = response.content
# saves as .wav file
with open('PDF/audio.wav', 'wb') as file:
    file.write(audio)

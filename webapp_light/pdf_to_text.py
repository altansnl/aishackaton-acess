from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
import sys, getopt
import re

#converts pdf, returns its text content as a string
def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close

    text = text.split("References")[0]
    text = text.split("REFERENCES")[0]

    text = text.split("Abstract")[1]
    try:
        text = text.split("ABSTRACT")[1]
    except IndexError:
        pass

    return text

def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

#converts all pdfs in directory pdfDir, saves all resulting txt files to txtdir
def convertMultiple(pdfDir, txtDir):
    if pdfDir == "": pdfDir = os.getcwd() + "\\" #if no pdfDir passed in 
    for pdf in os.listdir(pdfDir): #iterate through pdfs in pdf directory
        fileExtension = pdf.split(".")[-1]
        if fileExtension == "pdf":
            pdfFilename = pdfDir + pdf 
            text = convert(pdfFilename) #get string of text content of pdf
            textFilename = txtDir + pdf + ".txt"
            textFile = open(textFilename, "w") #make text file

            #text = text.replace("\n"," ")
            #text = strip_non_ascii(text)
            text = text.split("References")[0]
            text = text.split("REFERENCES")[0]

            text = text.split("Abstract")[1]
            try:
              text = text.split("ABSTRACT")[1]
            except IndexError:
              pass
            # text = ' '.join( [w for w in text.split() if (len(w)>1 or w=="a" or w=="A")])

            textFile.write(text) #write text to text file

import docHandler
import txtHandler
import pdfHandler
from textProcessor import textProcess

def formatChecker(location1, location2):
    try:
        format1 = location1[location1.rfind('.') + 1:].lower()
        try:
            format2 = location2[location2.rfind('.') + 1:].lower()
            if format1 in ['pdf', 'txt', 'doc', 'docx']:
                text1 = routeToHandler(format1, location1)
                if format2 in ['pdf', 'txt', 'doc', 'docx']: 
                    text2 = routeToHandler(format2, location2)
                    try:
                        return textProcess(text1, text2)
                    except:
                        print("Error from textProcessor Module! [Error issued from formatHandlers module]")
                else:
                    print(
                        "File 2 is of invalid format! [Error issued from formatHandlers module]")
            else:
                print(
                    "File 1 is of invalid format! [Error issued from formatHandlers module]")

        except:
            print(
                "Unexpected error occured! [Error issued from formatHandlers module]")
    except:
        print(
            "Unexpected error occured! [Error issued from formatHandlers module]")


def routeToHandler(format, location):
    if format == 'pdf':
        try:
            return pdfHandler.pdfProcess(location)
        except:
            print(
                "Error from pdfHandler module! [Error issued from formatHandler module]")
    elif format == 'txt':
        try:
            return txtHandler.textProcess(location)
        except:
            print("Error from txtHandler module! [Error issued from formatHandler module]")
    elif format == 'docx' or format == 'doc':
        try:
            return docHandler.docProcess(location)
        except:
            print(
                "Error from docHandler module! [Error issued from formatHandler module]")

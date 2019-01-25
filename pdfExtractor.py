from PyPDF2 import PdfFileReader

#
# Getting Metadata from a PDF using PyPDF2
#
"""
def get_info(path, mode):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
        author = info.author
        creator = info.creator
        producer = info.producer
        subject = info.subject
        title = info.title
        if mode == 'numPages':
            return number_of_pages
        if mode == 'info':
            return info
"""

#
# Extracting text from a PDF
#

def textExtract(path):
    try:
        with open(path, 'rb') as f:
            try:
                pdf = PdfFileReader(f)
                number_of_pages = pdf.getNumPages()
                text = ''
                for i in range(0, number_of_pages):
                    page = pdf.getPage(i)
                    text += ' '+page.extractText()
                    if __name__ == '__main__':
                        print('Page No.- '+str(i))
                        print(page)
                        print('Page type: {}'.format(str(type(page))))
                try:
                    if __name__ == '__main__':
                        print("Extracted text is:" + text)
                    else:
                        return text
                except:
                    print(
                        "Error while printing or returning result! [Error issued from pdfExtractor module]")
            except:
                print(
                    "Error while extracting data from PDF File! [Error issued from pdfExtractor module]")
    except:
        print(
            "Error while opening the file at provided path! [Error issued from pdfExtractor module]")


# DEBUG-PURPOSE
if __name__ == '__main__':
    path = 'abc.pdf'
    textExtract(path)

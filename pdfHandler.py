import pdfExtractor


def pdfProcess(location):
    try:
        text = pdfExtractor.textExtract(location)
        try:
            return text
        except:
            print(
                "Error while returning extracted text! [Error issued from pdfHandler module]")
    except:
        print(
            "Error from pdfExtractor module while extracting text from File! [Error issued from pdfHandler module]")
 
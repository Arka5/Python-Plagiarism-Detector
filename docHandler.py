import docExtractor

def docProcess(location):
    try:
        text = docExtractor.textExtract(location)
        try:
            return text
        except:
            print(
                "Error while returning extracted text! [Error issued from docHandler module]")
    except:
        print(
            "Error from docExtractor module while extracting text from File! [Error issued from docHandler module]")

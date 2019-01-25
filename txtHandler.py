import textExtractor

def textProcess(location):
    try:
        text = textExtractor.textExtract(location)
        try:
            return text
        except:
            print(
                "Error while returning extracted text! [Error issued from txtHandler module]")
    except:
        print(
            "Error from textExtractor module while extracting text from File! [Error issued from txtHandler module]")

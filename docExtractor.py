import docx2txt

def textExtract(location):
    try:
        return docx2txt.process(location)
    except:
        print("Error! Could not extract text from .docx file! [Error issued from docExtractor module]")

if __name__=='__main__':
    print(textExtract("def.docx"))
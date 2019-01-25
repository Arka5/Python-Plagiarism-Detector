#
# This module can extract text from a .txt file
#

def textExtract(location):
    try:
        file = open(location, "r")
        try:
            text = file.read()
            try:
                file.close()
                try:
                    return text
                except:
                    print(
                        "Error while returning result! [Error issued from textExtractor module]")
            except:
                print(
                    "Error while closing file! [Error issued from textExtractor module]")
        except:
            print(
                "File could not be read! [Error issued from textExtractor module]")
    except:
        print(
            "File could not be opened! [Error issued from textExtractor module]")

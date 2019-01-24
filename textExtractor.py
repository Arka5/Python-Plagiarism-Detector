#
# This module can extract text from a .txt file
#

from docAngleCalc import returnAngle


def textProcess(location1, location2):
    try:
        file1 = open(location1, "r")
        try:
            file2 = open(location2, "r")
            try:
                text1 = file1.read()
                try:
                    text2 = file2.read()
                    try:
                        result = returnAngle(text1, text2)
                        try:
                            file1.close()
                            try:
                                file2.close()
                                try:
                                    return result
                                except:
                                    print(
                                        "Error while returning result! [Error issued from textExtractor module]")
                            except:
                                print(
                                    "Error while closing file 2! [Error issued from textExtractor module]")
                        except:
                            print(
                                "Error while closing file 1! [Error issued from textExtractor module]")
                    except:
                        print(
                            "Error from docAngleCalc module! [Error issued from textExtractor module]")
                except:
                    print(
                        "File 2 could not be read! [Error issued from textExtractor module]")
            except:
                print(
                    "File 1 could not be read! [Error issued from textExtractor module]")
        except:
            print(
                "File 2 could not be opened! [Error issued from textExtractor module]")
    except:
        print(
            "File 1 could not be opened! [Error issued from textExtractor module]")

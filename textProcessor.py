import textExtractor
from docAngleCalc import returnAngle

def textProcess(text1, text2):
            try:
                return returnAngle(text1, text2)
            except:
                print(
                    "Error from docAngleCalc module! [Error issued from textProcessor module]")
#
# This is the main module in this project. It takes two locations as input and passes them to docLocator module
#
from docLocator import returnResult


def run():
    direct1 = input("Enter first file location: ")
    direct2 = input("Enter second file location: ")
    direct1 = direct1.strip()
    direct2 = direct2.strip()
    print("")
    try:
        result = str(int(returnResult(direct1, direct2)))+"%"
        print("Documents matched " + result)
    except:
        print("Error from docLocator module! [Error issued from main script]")


run()

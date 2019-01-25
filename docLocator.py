#
# This module can locate a document from a given location and checks if that document exists.
# If that documents exists in given location, it passes the location to formatHandlers module for further processing
# Otherwise, it throws an error
#

from formatHandlers import formatChecker


def getLocation(direct1, direct2):
    try:
        return formatChecker(direct1, direct2)
    except:
        print(
            "Error from formatHandlers module! [Error issued from docLocator module]")


def returnResult(direct1, direct2):
    try:
        return getLocation(direct1, direct2)*100
    except:
        print(
            "Internal error in docLocator module! [Error issued from docLocator module]")

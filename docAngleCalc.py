#
# This module can extract keywords from a given text
#

import re
import math


def extractKeywords(text):
    text = text.replace(',', ' ')
    text = text.replace('.', ' ')
    text = text.replace('\n', ' ')
    keywords = text.split(' ')
    if '' in keywords:
        keywords.remove('')
    if ' ' in keywords:
        keywords.remove(' ')
    return keywords


def getAngle(keywords1, keywords2):
    commonKeywords = []
    for keyword in keywords1:
        if keyword in keywords2:
            commonKeywords.append(keyword)
    return len(commonKeywords)/math.sqrt(len(keywords1)*len(keywords2))


def returnAngle(text1, text2):
    return(getAngle(extractKeywords(text1), extractKeywords(text2)))


if __name__ == '__main__':
    text1 = input()
    text2 = input()
    print(returnAngle(text1, text2))

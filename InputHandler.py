import re


def openFileAndReadData(fileName):
    handle = open(fileName, 'r', encoding='utf-8')
    data = handle.read()
    handle.close()
    return data


def PrepareText(text):
    reg = re.compile('[^A-Z]')
    return reg.sub('', text)

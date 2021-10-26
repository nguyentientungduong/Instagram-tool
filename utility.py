import csv
import random
try:
    from builtins import str
except ImportError as e:
    from __builtin__ import str

def get_test_data(filePath, separator=None):
    i = 0 
    with open(filePath, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        rawData = list(spamreader)
        testData = []
        if separator is None:
            separator = [1, len(rawData)]
        # print (rawData)
        for i in range(separator[0], separator[1]):
            testData.append(rawData[i])
    return testData

def get_test_data_random(filePath, separator=None):
    i = 0 
    with open(filePath, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        rawData = list(spamreader)
        testData = []
        if separator is None:
            separator = [1, len(rawData)]
        # print (rawData)
        for i in range(separator[0], separator[1]):
            testData.append(rawData[i])
    return random.choice(testData)

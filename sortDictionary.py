import json
from collections import OrderedDict

fileName = "sortedDictOfNames.json"


def dumpToJson(sortedDict):
    jsonDump = open(fileName, "w")
    jsonDump.write(json.dumps(sortedDict))
    jsonDump.close()


def sortDictionary():
    fileObj = open('names-nov_dec_2020.json')
    regDict = json.loads(fileObj.read())
    sortedDict = OrderedDict(sorted(regDict.items()))

    dumpToJson(sortedDict)


def main():
    sortDictionary()


if __name__ == "__main__":
    main()

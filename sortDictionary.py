from collections import OrderedDict
import json

fileName = "sortedDictOfNames.json"


def dumpToJson(soretdDict):
    jsonDump = open(fileName, "w")
    jsonDump.write(json.dumps(soretdDict))
    jsonDump.close()


def sortDictionary():
    fileObj = open('names-nov_dec_2020.json')
    regDict = json.loads(fileObj.read())
    soretdDict = OrderedDict(sorted(regDict.items()))

    dumpToJson(soretdDict)


def main():
    sortDictionary()


if __name__ == "__main__":
    main()

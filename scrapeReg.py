import requests
from bs4 import BeautifulSoup
import json

# Declarations
url = 'https://result.smuexam.in/ex25.php?eid=MARCH%202021%20SEMESTER%20EXAMINATIONS%20(FIRST%20YEAR%20ONLY)'
nextUrl = []  # subject URLs
header = {'User-Agent': 'Mozilla/5.0'}
fileName = url[28:30]  # dynamic filename


def getscrap():
    # declarations
    regList = []
    fullDict = {}  # full dictionary
    # create a new session
    session = requests.Session()
    # get cookie from entry point
    # cookie gets automatically stored in session
    html = session.get(url.strip(), headers=header)
    soup = BeautifulSoup(html.content, 'html.parser')

    for div in soup.find_all("div", {"class": "card-body"}):
        for paragraph in div.select("p"):
            for link in paragraph.select("a"):
                href = link['href']
                subcode = href[href.index('=') + 1:]
                nextUrl.append(
                    "https://result.smuexam.in/grade.php?subid=" + subcode)

    for urliter in nextUrl:
        count = 1
        code = "SUB"
        credit = 0.0
        reg = 0
        name = ""
        html = session.get(urliter.strip(), headers=header)
        soup = BeautifulSoup(html.content, 'html.parser')

        writeTextFile = open("{}.txt".format(fileName), "w")
        writeTextFile.write(soup.find('pre').getText())
        writeTextFile.close()

        readTextFile = open("{}.txt".format(fileName))
        line = readTextFile.readline()

        while line:
            # print(f"line1: {line}")
            line = line.strip().split()
            # print(f"line2: {line}")

            if((len(line) > 0 and line[0] == "File") or (len(line) > 0 and (line[0] == "P>35" or line[2] == "F<35" or line[0] == "Last" or line[0] == "/UNIVERSAL"))):
                break
            elif (len(line) == 0 or line[0][0:3] == "REG" or line[0][0:3] == "SIK" or line[0][0:3] == "GRA" or line[0][
                0:3] == "Abb" or
                    line[0][0:3] == "Abs" or line[0][0:3] == "S>=" or line[0][0:3] == "P>=" or line[0][0:3] == "Sto" or
                    line[0][0:3] == "Gra"):
                line = readTextFile.readline()
                continue
            elif (line[0] == "Subject"):
                if (line[1] == "Code"):
                    code = line[3]
                elif (line[1] == "Title"):
                    i = 3
                    while (i < len(line)):
                        name += line[i] + " "
                        i += 1
                elif (line[1] == "Credit"):
                    if len(line) >= 4:
                        credit = float(line[3][0:3])
            else:
                Dict = {}  # subject iteration
                # print(f"reg: {reg}")
                if line[0] == "S>89," or line[0] == "Lower":
                    break

                reg = int(line[0])
                fullDict[reg] = fullDict.get(reg, {})
                fullDict[reg][""] = ""
            line = readTextFile.readline()

        readTextFile.close()

    jsonDump = open("{}.json".format(fileName), "w")
    jsonDump.write(json.dumps(fullDict))
    jsonDump.close()


if __name__ == "__main__":
    getscrap()

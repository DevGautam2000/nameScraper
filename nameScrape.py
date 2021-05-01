from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

import json

uri = "https://result.smuexam.in/search.php?eid=NOVEMBER/DECEMBER%20SEMESTER%20EXAMINATION%202020&examType=202"
fileObj = open('23.json')
regDict = json.loads(fileObj.read())
fileName = "names-nov_dec_2020"
namesDict = {}


def getNames(reg):
    driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
    wait = WebDriverWait(driver, 10)

    driver.get(uri)

    driver.refresh()

    driver.find_element_by_xpath(
        "//input[@name='search']").send_keys(reg)

    driver.find_element_by_xpath(
        "//button[@class='searchButton']") .click()

    text2 = wait.until(
        presence_of_element_located((By.XPATH, "//section[@id='portfolio']/div/div/div[1]")))

    text2 = text2.text.split("\n")

    if len(text2) > 1:
        namesDict[reg] = namesDict.get(reg, {})
        joinString = text2[2]
        joinString = joinString.split(":")

        name = joinString[1].strip()
        # print(name)  # print statement here
        namesDict[reg]['name'] = name

        # print(namesDict)

    driver.close()


def main():
    for reg in regDict:
        getNames(reg)

    jsonDump = open("{}.json".format(fileName), "w")
    jsonDump.write(json.dumps(namesDict))
    jsonDump.close()


if __name__ == "__main__":
    main()

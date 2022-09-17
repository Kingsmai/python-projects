from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv

MASTER_CLASSNAME = '_3Bc7H.g0rxnol2.thghmljt.p357zi0d.ggj6brxn.f8m0rgwh.gfz4du6o.ag5g9lrv.bs7a17vp.ov67bkzj'

# The scrollable element
MASTER_ELEMENT = f'#app > div > span:nth-child(2) > div > span > div > div > div > div > div > div > div.{MASTER_CLASSNAME}'

MASTER_HEIGHT_ELEMENT = f'#app > div > span:nth-child(2) > div > span > div > div > div > div > div > div > div.{MASTER_CLASSNAME} > div > div > div'

LIST_ITEM_HEIGHT = 72

ITEM_ELEMENT = f'#app > div > span:nth-child(2) > div > span > div > div > div > div > div > div > div.{MASTER_CLASSNAME} > div > div > div > div'


driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com")

print('''
User Manual:
1. Login to Whatsapp
2. Open the group you need to scrap
3. Click the ... on the top right corner
4. Scroll down and click "Show all members"''')

print('Press ENTER when you are done')
input('> ')

fileName = driver.find_element(By.CSS_SELECTOR, '#main > header > div._24-Ff > div._2rlF7 > div > span').text

master_element = driver.find_element(By.CSS_SELECTOR, MASTER_ELEMENT)

masterHeightElement = driver.find_element(By.CSS_SELECTOR, MASTER_HEIGHT_ELEMENT)
maxHeight = int(masterHeightElement.get_attribute('style').split(':')[-1][:-3])
height = 0

field = ['Contact', 'About', 'Public Name']
contactList = {}

print(maxHeight)

while height <= maxHeight + (LIST_ITEM_HEIGHT * 18):
    nameListElementDict = {}
    itemList = driver.find_elements(By.CSS_SELECTOR, ITEM_ELEMENT)
    for idx, item in enumerate(itemList):
        # Get element child
        itemTransformValue = item.get_attribute('style').split(';')[-2].split(':')[-1]
        nameListElementDict[f'{idx + 1}'] = int(itemTransformValue[12:-3])
    nameListElementDict = {k: v for k, v in sorted(nameListElementDict.items(), key=lambda item: item[1])}
    for idx, nthChild in enumerate(nameListElementDict.keys()):
        if idx == 9:
            break
        currentElementChild = driver.find_element(By.CSS_SELECTOR, ITEM_ELEMENT + f':nth-child({nthChild}) > div')
        if currentElementChild.get_attribute('class') != 'YGe90 MCwxg':
            contactNumberSelector = f'#app > div > span:nth-child(2) > div > span > div > div > div > div > div > div > div.{MASTER_CLASSNAME} > div > div > div > div:nth-child({nthChild}) > div > div > div._3OvU8 > div._3vPI2 > div > span'
            aboutParentSelector = f'#app > div > span:nth-child(2) > div > span > div > div > div > div > div > div > div.{MASTER_CLASSNAME} > div > div > div > div:nth-child({nthChild}) > div > div > div._3OvU8 > div._37FrU > div._1qB8f'  # > span
            nameParentSelector = f'#app > div > span:nth-child(2) > div > span > div > div > div > div > div > div > div.{MASTER_CLASSNAME} > div > div > div > div:nth-child({nthChild}) > div > div > div._3OvU8 > div._37FrU > div._1i_wG'  # > span._1ux8Y > span'
            contactNumber = driver.find_element(By.CSS_SELECTOR, contactNumberSelector).text
            aboutParent = driver.find_element(By.CSS_SELECTOR, aboutParentSelector).text
            if aboutParent != '':
                aboutSelector = f'#app > div > span:nth-child(2) > div > span > div > div > div > div > div > div > div.{MASTER_CLASSNAME} > div > div > div > div:nth-child({nthChild}) > div > div > div._3OvU8 > div._37FrU > div._1qB8f > span'
                about = driver.find_element(By.CSS_SELECTOR, aboutSelector).text
            else:
                about = ''
            nameParent = driver.find_element(By.CSS_SELECTOR, nameParentSelector).text
            if nameParent != '':
                nameParentSelector = f'#app > div > span:nth-child(2) > div > span > div > div > div > div > div > div > div.{MASTER_CLASSNAME} > div > div > div > div:nth-child({nthChild}) > div > div > div._3OvU8 > div._37FrU > div._1i_wG > span._1ux8Y > span'
                name = driver.find_element(By.CSS_SELECTOR, nameParentSelector).text
            else:
                name = ''
            contactList[contactNumber] = [contactNumber, about, name]
        else:
            # Skip the 'ABC' category label
            continue
    # Scroll down to next page
    driver.execute_script(f'arguments[0].scrollBy(0, {LIST_ITEM_HEIGHT * 9})', master_element)
    height += LIST_ITEM_HEIGHT * 9
    print(height)
    time.sleep(1)

driver.close()

with open(f'Output/{fileName}.csv', 'w', encoding='utf-8', newline='') as outputFile:
    writer = csv.writer(outputFile)

    writer.writerow(field)
    for record in contactList.values():
        writer.writerow(record)
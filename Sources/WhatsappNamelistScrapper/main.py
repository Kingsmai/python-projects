# Written by: Xiaomai & Reyos

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv


"""
USE AT YOUR OWN RISK
"""

# If selenium.common.exceptions.NoSuchElementException thrown, change this classname to the newest one.
MASTER_CLASSNAME = '_3Bc7H.g0rxnol2.thghmljt.p357zi0d.ggj6brxn.f8m0rgwh.gfz4du6o.ag5g9lrv.bs7a17vp.ov67bkzj'
EMPTY_ITEM = 'YGe90 MCwxg'
HISTORY_BTN = 'p357zi0d ktfrpxia nu7pwgvd ac2vgrno sap93d0t gndfcl4n k45dudtp enbbiyaj jq3rn4u7 ihvf49ua os03hap6'

# The scrollable container
MASTER_ELEMENT = f'#app > div > span:nth-child(2) > div > span > div > div > div > div > div > div > div.{MASTER_CLASSNAME}'
# Use to get the height data
MASTER_HEIGHT_ELEMENT = f'{MASTER_ELEMENT} > div > div > div'
# Each Item
ITEM_ELEMENT = f'{MASTER_HEIGHT_ELEMENT} > div'
# The height of each list item
LIST_ITEM_HEIGHT = 72
PAGE_HEIGHT = LIST_ITEM_HEIGHT * 18

CHAT_NAME_ELEMENT = '#main > header > div._24-Ff > div._2rlF7 > div > span'

driver = webdriver.Firefox()
driver.get('https://web.whatsapp.com')
print('''
User Manual:
1. Login to Whatsapp
2. Open the group you need to scrap
3. Click the ... on the top right corner
4. Scroll down and click "Show all members"''')

print('Press ENTER when you are done')
input('> ')

fileName = driver.find_element(By.CSS_SELECTOR, CHAT_NAME_ELEMENT).text
masterElement = driver.find_element(By.CSS_SELECTOR, MASTER_ELEMENT)
masterHeight = int(driver.find_element(By.CSS_SELECTOR, MASTER_HEIGHT_ELEMENT).get_attribute('style').split(':')[-1][:-3])

specialChars = "!#$%^&*/" 
for specialChar in specialChars:
    fileName = fileName.replace(specialChar, '-')

while True:
    contactList = {}
    currentHeight = 0
    while currentHeight <= masterHeight:
        print(f'{currentHeight} / {masterHeight}')
        nameList = driver.find_elements(By.CSS_SELECTOR, ITEM_ELEMENT)
        print(len(nameList))
        for nthChild, nameItem in enumerate(nameList):
            if nameItem.get_attribute('class') != EMPTY_ITEM:
                detailParentSelector = f'{ITEM_ELEMENT}:nth-child({nthChild + 1}) > div'
                detailParentClass = driver.find_element(By.CSS_SELECTOR, detailParentSelector).get_attribute('class')
                if detailParentClass == EMPTY_ITEM or detailParentClass == HISTORY_BTN:
                    continue
                detailSelector = f'{detailParentSelector} > div > div._3OvU8'
                contactAdminSelector = f'{detailSelector} > div._3vPI2 > div' # Ppl is admin if got len of 2
                contactSelector = f'{contactAdminSelector} > span' # Number
                aboutParentSelector = f'{detailSelector} > div._37FrU > div._1qB8f'
                nameParentSelector = f'{detailSelector} > div._37FrU > div._1i_wG'
                contact = driver.find_element(By.CSS_SELECTOR, contactSelector).text
                if driver.find_element(By.CSS_SELECTOR, aboutParentSelector).text != '':
                    about = driver.find_element(By.CSS_SELECTOR, f'{aboutParentSelector} > span').text
                else: 
                    about = ''
                if driver.find_element(By.CSS_SELECTOR, nameParentSelector).text != '':
                    name = driver.find_element(By.CSS_SELECTOR, f'{nameParentSelector} > span._1ux8Y > span').text
                else:
                    name = ''
                contactList[contact] = [
                    contact,
                    about,
                    name,
                    len(driver.find_elements(By.CSS_SELECTOR, contactAdminSelector)) == 2
                ]
        driver.execute_script(f'arguments[0].scrollBy(0, {PAGE_HEIGHT})', masterElement)
        currentHeight += PAGE_HEIGHT
        time.sleep(0.8)

    field = ['Contact', 'About', 'Name', 'isAdmin']

    with open(f'Output/{fileName}.csv', 'w', encoding='utf8', newline='') as outputFile:
        writer = csv.writer(outputFile)
        writer.writerow(field)
        for name in contactList:
            writer.writerow(contactList[name])

    print('Continue? (Y/n)')
    if not input('> ').casefold().startswith('y'):
        break


print("Written By: Xiaomai & Reyos")

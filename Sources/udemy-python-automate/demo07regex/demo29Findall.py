import re
from re import findall
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
resume = '''
Mobile: 419-555-1234
Mobile: 415-555-7890
Phone: 437-789-6516
Fax: 1238-720-0516
'''
print(phoneRegex.search(resume)) # Only return a Match Object
print(phoneRegex.findall(resume)) # return a list of string
print()

# With ZERO or ONE groups
phoneRegex = re.compile(r'(\d\d\d)-\d\d\d-\d\d\d\d')
print(phoneRegex.findall(resume)) # return a list of string

# With TWO or MORE groups
phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
print(phoneRegex.findall(resume)) # return a list of tuples of strings
print()

phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
print(phoneRegex.findall(resume)) # return a list of tuples of strings

# Character class
lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking, 7 swans a swimming, 6 geese a laying, 5 gold rings, 4 calling birds, 3 french hens, 2 turtle doves and a partridge in a pear tree walk into a bar.'
xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics))

# Create own character class
vowelRegex = re.compile(r'[aeiouAEIOU]') # r'(a|e|i|o|u)'
print(vowelRegex.findall('Robocop eats baby food.'))
doubleVovelRegex = re.compile(r'[aeiouAEIOU]{2}')
print(doubleVovelRegex.findall('Robocop eats baby food.'))

# Negative character class
consonantsRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantsRegex.findall('Robocop eats baby food.'))

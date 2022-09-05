import re
from re import DOTALL, findall

# ^ Stands for search at the beginning of the string.
startWithHelloRegex = re.compile(r'^Hello')
mo = startWithHelloRegex.search("Hello there!")
print(mo) # <re.Match object; span=(0, 5), match='Hello'>
mo = startWithHelloRegex.search("He said: 'Hello!'")
print(mo) # None

# $ Stands for search at the ending of the string.
endWithWorldRegex = re.compile(r'World!$')
mo = endWithWorldRegex.search("Hello World!")
print(mo) # <re.Match object; span=(6, 12), match='World!'>
mo = endWithWorldRegex.search("Hello World! nice to meet you.")
print(mo) # None

# ^both$ means pattern must match the entire string
allDigitsRegex = re.compile(r'^\d+$')
mo = allDigitsRegex.search('314159265359')
print(mo) # <re.Match object; span=(0, 12), match='314159265359'>
mo = allDigitsRegex.search('31415x265359')
print(mo) # None

# . Stands for anything expect newline
atRegex = re.compile(r'.at')
mo = atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo) # ['cat', 'hat', 'sat', 'lat', 'mat']
atRegex = re.compile(r'.{1,2}at')
mo = atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo) # [' cat', ' hat', ' sat', 'flat', ' mat']

# .* to match Anything (greedy)
print('First Name: Andrew, Last Name: Xiaomai'.find(":")) # 10
print('First Name: Andrew, Last Name: Xiaomai'.find(":") + 2) # 1
print('First Name: Andrew, Last Name: Xiaomai'[12:]) # Andrew, Last Name: Xiaomai
nameRegex = re.compile(r'First Name: (.*), Last Name: (.*)')
mo = nameRegex.findall('First Name: Andrew, Last Name: Xiaomai')
print(mo) # [('Andrew', 'Xiaomai')]

# .*? match Anything (non-greedy)
serve = '<To serve humans> for dinner>'
nonGreedyRegex = re.compile(r'<(.*?)>')
mo = nonGreedyRegex.findall(serve)
print(mo) # ['To serve humans']
greedyRegex = re.compile(r'<(.*)>')
mo = greedyRegex.findall(serve)
print(mo) # ['To serve humans> for dinner']

# re.DOTALL flag means '.' include newlines
prime = 'Serve the public trust.\nProtect the innocent.\nUpload the law.'
dotStarRegex = re.compile(r'.*')
mo = dotStarRegex.search(prime)
print(mo) # re.Match object; span=(0, 23), match='Serve the public trust.'>
dotStarRegex = re.compile(r'.*', re.DOTALL)
mo = dotStarRegex.search(prime)
print(mo) # <re.Match object; span=(0, 61), match='Serve the public trust.\nProtect the innocent.\nU>

# re.IGNORECASE or re.I
vowelRegex = re.compile(r'[aeiou]')
mo = vowelRegex.findall('Al, why does your programming book talk about RoboCop so much?')
print(mo)
vowelRegex = re.compile(r'[aeiou]', re.I) # or re.IGNORECASE
mo = vowelRegex.findall('Al, why does your programming book talk about RoboCop so much?')
print(mo)
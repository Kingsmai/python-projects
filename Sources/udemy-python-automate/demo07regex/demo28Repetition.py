import re

# Symbol ? stand for 0 or 1 time
batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search("The Adventure of Batman")
print(mo.group())
mo = batRegex.search("The Adventure of Batwoman")
print(mo.group())
mo = batRegex.search("The Adventure of Batwowowoman")
print(mo == None) # True, check for "wo" appear one time only

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneRegex.search("My phone number is 415-999-1234. Call me tomorrow.")
print(mo.group())
mo = phoneRegex.search("My phone number is 999-1234. Call me tomorrow.")
print(mo == None) # True, Pattern not found.
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search("My phone number is 999-1234. Call me tomorrow.")
print(mo.group())

# to include question mark, put a slash in front of the question mark
dinnerRegex = re.compile(r'dinner\?')
mo = dinnerRegex.search("Shall we have a dinner?")
print(mo.group())

# Symbol * stands for 0 or more times.
batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search("The Adventure of Batman")
print(mo.group())
mo = batRegex.search("The Adventure of Batwoman")
print(mo.group())
mo = batRegex.search("The Adventure of Batwowowoman")
print(mo.group())

# to include asterisk, put a slash in front of the asterisk
asteriskRegex = re.compile(r'asterisk\*')
mo = asteriskRegex.search("Hmm... the asterisk* will be found!")
print(mo.group())

# Symbol + stands for 1 or more times.
batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search("The Adventure of Batman")
print(mo == None) # True, "wo" must be at least one time.
mo = batRegex.search("The Adventure of Batwoman")
print(mo.group())
mo = batRegex.search("The Adventure of Batwowowoman")
print(mo.group())

# to include plus, put a slash in front of the plus
plusRegex = re.compile(r'2\+2')
mo = plusRegex.search("What is the answer of 2+2")
print(mo.group())

# {x} stands for exactly x times.
haRegex = re.compile(r'(Ha){3}') # Match "ha" for 3 times.
mo = haRegex.search("He say:'HaHaHa'")
print(mo.group())

phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(, )?){3}') # Match "phone" for 3 times.
mo = phoneRegex.search("My numbers are 415-555-1234, 555-4242, 212-555-0000")
print(mo.group())

# {x,y} stands for at least x at most y
haRegex = re.compile(r'(Ha){3,5}') # Match "ha" between 3 - 5 times.
mo = haRegex.search("He say:'HaHaHaHa'")
print(mo.group())
mo = haRegex.search("He say:'HaHaHaHaHaHaHaHa'")
print(mo.group()) # it still matches because it return the first five it meet

# {x,} stand for x or more
# {,y} stand for 0 to y

# Practise
digitRegex = re.compile(r'(\d){3,5}')
mo = digitRegex.search("1234567890")
print(mo.group()) # 12345, Return the first five, and greedy match (as long as possible matches)

# non greedy match
digitRegex = re.compile(r'(\d){3,5}?')
mo = digitRegex.search("1234567890")
print(mo.group()) # 123
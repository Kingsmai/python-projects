import re # import re module


phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999 for my office line.'

# matchObject = phoneNumberRegex.search(message)
# print(matchObject.group)

mo = phoneNumberRegex.findall(message) # Return a list of matched regex
print(mo)

# Regex group
# use the parentheses to group the regex
phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
message = 'My phone number is 415-555-4242'
mo = phoneNumberRegex.search(message)
print(mo.group())
print(mo.group(1))
print(mo.group(2))

# To search with the parentheses
phoneNumberRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
message = 'My phone number is (415) 555-4242'
mo = phoneNumberRegex.search(message)
print(mo.group())

# With pipe "|" character, you can search for any possible matches
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
mo = batRegex.search('Batmotorcycle lost a wheel')
print(mo == None) # True

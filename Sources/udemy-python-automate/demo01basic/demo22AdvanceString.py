# Escape character
# When we used to use some characters that are otherwise impossible to put into:
# print('That is Alice's cat.') # SyntaxError: invalid syntax
# To conquer this, we may:
print("That is Alice's cat.")
# But sometimes, we need to use both "" and '' (or something else)
# Here goes the escape characters!
print('That is Alice\'s cat.') # Just put a \backslash in front of the character, then magic will happen
# Here goes the lists:
# Escape character  Print as
# \'                Single quote
# \"                Double quote
# \t                Tab
# \n                Newline (line break)
# \\                backslash
print('Hello there!\nHow are you?\nI\'m fine.')

# Raw string: type a 'r' before the string and it will ignore the escape character
print(r'That is Carol\'s cat.')

# Multiline string: String inside both """ or '''
spam = '''
Dear Alice,
Eve's has been arrested for catnapping, cat burglary, and extortion.
Sincerely,
Bob.
'''
print(spam) # Also can be output directly
print(len(spam)) # Print the length of spam string

# Similar with list:
spam = 'Hello World'
print(spam[0]) # it will print the first character
print(spam[1:5])
print(spam[-1]) # print the last character
print('Hello' in spam) # True
print('hello' in spam) # False, case-sensitive
print('x' in spam) # False
spam = 'Hello world!'
print(spam.upper()) # HELLO WORLD!
# String is not mutable so spam still contain the basic one
print(spam)
# To modify it, just
spam = spam.upper()
print(spam)
print(spam.lower()) # hello world!

# May use lower and upper method to preforming case-insensitive judgement
answer = 'YES'
print(answer == 'yes') # False
print(answer.lower() == 'yes') # True

# To determine weather the string is uppercase or lowercase:
spam = 'Hello world!'
print(spam.islower()) # False, because H is uppercase
spam = 'hello world!'
print(spam.islower()) # True
spam = 'HELLO WORLD!'
print(spam.isupper()) # True
# Since it have not letters inside the string or it is blank, it will return false:
print(''.islower()) # True
print(''.isupper()) # True
print('12345'.islower()) # False
print('12345'.isupper()) # False

# Other is- method
# Method        Tests
# isalpha()     letter only
# isalnum()     letter and number only
# isdecimal()   number only
# isspace()     whitespace only
# istitle()     titlecase only
print('Hello'.isalpha()) # True
print('Hello123'.isalpha()) # False
print('Hello123'.isalnum()) # True
print('123'.isdecimal()) # True
print('        '.isspace()) # True
print('Hello world!'.isspace()) # False
print('Hello world!'[5].isspace()) # True
print('This Is Title Case.'.istitle()) # True

# title method
print("hello world!".title()) # Hello World!

# startswith and endswith method
print('Hello world!'.startswith('Hello')) # True
print('Hello world!'.startswith('H')) # True
print('Hello world!'.startswith('ello')) # False
print('Hello world!'.endswith('world!')) # True
print('Hello world!'.endswith('world')) # False

# join method join the list items
print(','.join(['cats', 'rats', 'bats']))
print(''.join(['cats', 'rats', 'bats']))
print(' '.join(['cats', 'rats', 'bats']))
print('\n\n'.join(['cats', 'rats', 'bats']))

# split method split the list items
print('My name is Xiaomai'.split())
print('My name is Xiaomai'.split('m')) # to split between letter m

# ljust and rjust method: add justify into the string
print("==================================")
print('Hello'.rjust(10))
print(len('Hello'.rjust(10)))
print('Hello'.ljust(20))
print(len('Hello'.ljust(20)))
# fills with pattern character (just one)
print('Hello'.rjust(20, '*'))
print('Hello'.ljust(25, '-'))
# center method, both add left and right justify:
print('Hello'.center(20))
print('Hello'.center(20, '='))

# strip, rstrip and lstrip method: remove the white space
spam = 'Hello'.rjust(10)
print(spam)
print(spam.strip()) # it will return a brand new string
print(spam)
spam = spam.strip()
print(spam)
spam = 'Hello'.center(20)
print(spam.lstrip()) # remove left space
print(spam.rstrip()) # remove right space
print('SpamSpamBaconSpamEggsSpamSpam'.strip('ampS'))

# replace method: replace the specify character with another character
print('Hello there'.replace('e', 'XYZ'))

# Using pyperclip module to copy the text to your computer clipboard
# pyperclip is a thirdparty module that didn't come with Python
# you must install it manually
# locate to your Python installation dir and open up Scripts directory in CMD
# type: pip.exe install pyperclip and wait for install
import pyperclip
pyperclip.copy('Hello!!!!!!!') # you now can paste this string outside Python
print(pyperclip.paste()) # paste the item which already on clipboard
import re
nameRegex = re.compile(r'Agent \w+')
mo = nameRegex.findall("Agent Alice gave the secret documents to Agent Bob.")
print(mo) # ['Agent Alice', 'Agent Bob']

# replace the word in the sentence
mo = nameRegex.sub("REDACTED", "Agent Alice gave the secret documents to Agent Bob.")
print(mo) # REDACTED gave the secret documents to REDACTED.

# Using \1 \2 etc in sub()
nameRegex = re.compile(r'Agent (\w)\w*')
mo = nameRegex.findall("Agent Alice gave the secret documents to Agent Bob.")
print(mo) # ['A', 'B']
mo = nameRegex.sub(r"Agent \1****", "Agent Alice gave the secret documents to Agent Bob.") # \1 means the first in the group
print(mo) # Agent A**** gave the secret documents to Agent B****.

# verbose mode
phoneRegex = re.compile(r'''
(\d\d\d-)|     # area code (without parenthesis, with dash)
(\(\d\d\d\) )  # -or- area code (with parenthesis, without dash)
\d\d\d      # first 3 digit
-           # second dash
\d\d\d\d    # last 4 digit
\sx\d{2,4}  # extension, like x1234
''', re.VERBOSE | re.IGNORECASE | re.DOTALL) # combine multiple flags using |
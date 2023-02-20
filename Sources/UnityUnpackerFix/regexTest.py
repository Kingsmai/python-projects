import re


def find_word(s):
    pattern = re.compile(r'\b[a-zA-Z]+\b')
    match = pattern.search(s)
    if match:
        return match.group()
    else:
        return None


print(find_word("w404"))
print(find_word("ice_floor_0"))

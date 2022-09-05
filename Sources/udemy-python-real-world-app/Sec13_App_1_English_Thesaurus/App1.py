import json
# Python 3 standard library lists
# https://docs.python.org/3/library/index.html
# import difflib
from difflib import SequenceMatcher # import SequenceMatcher method from difflib
from difflib import get_close_matches

data = json.load(open("data.json")) # load the json file
# print(data) # Debug: print out the whole json file
# print(data["rain"]) # Debug: print out the data(dict)'s phrase

def translate(word):
    # convert the word into lowercase
    word = word.lower()
    if word in data: # See whether word is exist in data
        return data[word]
    elif word.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[word.title()]
    elif word.upper() in data: #in case user enters words like USA or NATO
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0: # get_close_matches returns a list
        choice = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0]) # get the first word from the list
        if choice == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif choice == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We couldn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
def sentence_maker(phrase):
    # phrase = ''
    interrogatives = ("how", "what", "why")
    capitalized = phrase.capitalize()
    # Add questionmark to the sentence
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

print(sentence_maker("how are you"))

# The final sentence result
results = []

# Getting user input
while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))

print(" ".join(results))
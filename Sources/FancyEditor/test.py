# Get a tag name
def process(taggedString: str):
    currentTag = ''
    tagList = []

    for ch in taggedString:
        if ch == '<':
            isTag = True
        if isTag:
            currentTag += ch
        if ch == '>':
            isTag = False
            tagList.append(currentTag)
            currentTag = ''
    print(tagList)


sampleString = r'<bold>Hello,</bold> <italic>world</italic>!'
translatedString = process(sampleString)
print(translatedString)

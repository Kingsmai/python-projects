
# typeTag
BOLD = 'bold'
ITALIC = 'italic'
BOLD_ITALIC = 'botalic'
SCRIPT = 'script'
BOLD_SCRIPT = 'bscript'
FRAKTUR = 'fraktur'
DOUBLE_STRUCK = 'double'
BOLD_FRAKTUR = 'bfraktur'
SANS_SERIF = 'sans'
BOLD_SANS_SERIF = 'bsans'
ITALIC_SANS_SERIF = 'isans'
BOLD_ITALIC_SANS_SERIF = 'bisans'
MONOSPACE = 'mono'

CODEPOINT_OF_A = {
    BOLD: 119808,
    ITALIC: 119860,
    BOLD_ITALIC: 119912,
    SCRIPT: 119964,
    BOLD_SCRIPT: 120016,
    FRAKTUR: 120068,
    DOUBLE_STRUCK: 120120,
    BOLD_FRAKTUR: 120172,
    SANS_SERIF: 120224,
    BOLD_SANS_SERIF: 120276,
    ITALIC_SANS_SERIF: 120328,
    BOLD_ITALIC_SANS_SERIF: 120380,
    MONOSPACE: 120432,
}

def process(taggedString: str):
    translatedString = ''
    tagStack = []
    currentTag = ''
    tagStart = False
    for ch in taggedString:
        if ch == '<':
            currentTag += ch
            tagStart = True
            continue
        if ch == '>':
            currentTag += ch
            tagStart = False
            if '/' not in currentTag:
                tagStack.append(currentTag)
            else:
                tagStack.pop()
            currentTag = ''
            continue
        if tagStart:
            currentTag += ch
            continue
        if len(tagStack) > 0:
            tag = tagStack[-1][1:-1]
            translatedString += convertCharacter(ch, tag)
        else:
            translatedString += ch
    return translatedString


def convertCharacter(ch, font):
    offset = getCharacterOffset(ch)
    if ch >= 'A' and ch <= 'Z':
        return chr(offset + CODEPOINT_OF_A[font])
    elif ch >= 'a' and ch <= 'z':
        return chr(offset + CODEPOINT_OF_A[font] + 26)
    else:
        return ch


def getCharacterOffset(baseCharacter: str):
    codepoint = ord(baseCharacter)
    if baseCharacter >= 'A' and baseCharacter <= 'Z':
        offset = codepoint - ord('A')
    elif baseCharacter >= 'a' and baseCharacter <= 'z':
        offset = codepoint - ord('a')
    else:
        offset = codepoint
    return offset


if __name__ == '__main__':
    sampleString = r'<bold>Hello,</bold> <italic>world</italic>!'
    # sampleString = r'Hello, world!'
    translatedString = process(sampleString)
    print(translatedString)

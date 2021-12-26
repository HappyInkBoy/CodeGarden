text = input('I am a translator, enter a message below to be translated into morse code:\n')

morseDictionary = {
    "a" : '.-',
    "b" : '-...',
    "c" : '-.-.',
    "d" : '-..',
    "e" : '.',
    "f" : '..-.',
    "g" : '--.',
    "h" : '....',
    "i" : '..',
    "j" : '.---',
    "k" : '-.-',
    "l" : '.-..',
    "m" : '--',
    "n" : '-.',
    "o" : '---',
    "p" : '.--.',
    "q" : '--.-',
    "r" : '.-.',
    "s" : '...',
    "t" : '-',
    "u" : '..-',
    "v" : '...-',
    "w" : '.--',
    "x" : '-..-',
    "y" : '-.--',
    "z" : '..--'
}

reverseMorseDictionary = {v: k for k, v in morseDictionary.items()}

text = text + " "
result = ""
token = ""
for toot in text:
    if toot in morseDictionary:
        result = result + " " + morseDictionary[toot]
    elif toot == "." or toot == "-":
        token = token + toot
    elif toot == " ":
        result = result + " "
        if token != "":
            result = result + reverseMorseDictionary[token]
            token = ""
print (result)

text = input('I am a translator, translate morse code with me (if you are writing in morse code, remember to start the message with a space):\n')

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
print (reverseMorseDictionary)

def alpha2Morse (letter):
    if letter in morseDictionary:
        return morseDictionary[letter]
    elif letter in reverseMorseDictionary:
        return reverseMorseDictionary[letter]
    else:
        return ' '

result = ""

for toot in text:
    result = result + ' ' + alpha2Morse (toot)
print (result)

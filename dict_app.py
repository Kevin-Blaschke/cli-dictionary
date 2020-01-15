import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input('Perhaps you meant %s instead of %s? \n' % (get_close_matches(word, data.keys())[0],word))
        if yn.lower() == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == 'N':
            return 'The word does not exist. Please double check. \n'
        else:
            return 'Error: Invalid input. Please double check. \n'
    else:
        return 'The word does not exist. Please double check. \n'

while True:
    word = input('Enter word: ')

    output = translate(word)

    if type(output) == list:
        for item in output:
            print(item + '\n')
    else:
        print(output + '\n')

    next = input('Would you like to try another word? ')
    if next.lower() == 'y' or next.lower() == 'yes':
        continue
    else:
        break

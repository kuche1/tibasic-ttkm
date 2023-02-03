#! /usr/bin/env python3

def shlokavaise_char(char:str)->str:
    char = char.lower()

    if char in 'abcdefghijklmnopqrstuvwxyz':
        return char

    r = None
    match char:
        # specialni bes conversiq
        case ' ': r=char
        case '=': r=char
        case ',': r=char
        case '-': r=char
        case '.': r=char
        case '(': r=char
        case ')': r=char
        case '[': r=char
        case ']': r=char
        case '?': r=char
        # specialni s konversiq
        case '\uf057': r='(ohm)'
        case '\uf06d': r='(micro)'
        case '”': r="'"
        case '“': r="'"
        # cifro
        case '0': r=char
        case '1': r=char
        case '2': r=char
        case '3': r=char
        case '4': r=char
        case '5': r=char
        case '6': r=char
        case '7': r=char
        case '8': r=char
        case '9': r=char
        # bulgarski
        case 'а': r='a'
        case 'б': r='b'
        case 'в': r='v'
        case 'г': r='g'
        case 'д': r='d'
        case 'е': r='e'
        case 'ж': r='j'
        case 'з': r='z'
        case 'и': r='i'
        case 'й': r='i'
        case 'к': r='k'
        case 'л': r='l'
        case 'м': r='m'
        case 'н': r='n'
        case 'о': r='o'
        case 'п': r='p'
        case 'р': r='r'
        case 'с': r='s'
        case 'т': r='t'
        case 'у': r='u'
        case 'ф': r='f'
        case 'х': r='h'
        case 'ц': r='c'
        case 'ч': r='4'
        case 'ш': r='6'
        case 'щ': r='6t'
        case 'ъ': r='u'
        case 'ю': r='u'
        case 'я': r='q'
    assert r != None, f'{char=}'
    return r

def shlokavaise(vup:str)->str:
    result = ''
    for char in vup:
        char = shlokavaise_char(char)
        result += char
    return result

result = ''

while True:
    try:
        vup = input('> ')
    except EOFError:
        break
    vup_en = shlokavaise(vup)
    result += vup_en

print('result:')
print(result)


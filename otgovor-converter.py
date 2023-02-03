#! /usr/bin/env python3

def shlokavaise_char(c:str)->str:

    # common
    if c.lower() in '01234567890abcdefghijklmnopqrstuvwxyz =,-.()[]?*/%+:;-|':
        return c

    # special
    match c:
        case '\uf057': return '(ohm)'
        case '\uf06d': return '(micro)'
        case '”': return "'"
        case '“': return "'"
        case '–': return '-'

    is_lower = c.lower() == c

    # bulgarski
    r = None
    match c.lower():
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

    assert r != None, f'{c=}'

    if not is_lower:
        r = r.upper()

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


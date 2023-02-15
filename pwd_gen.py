from re import search
from random import sample

while True:
    
    try:
        n = int(input('Password Length: ').strip())
        if n <= 0:
            continue
        else:
            break
    
    except ValueError:
        print('Only numbers allowed')
        continue


while True:
    
    pwd = "".join(sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                            '0123456789`~!@#$%^&*()_+-={}[]:";\'<>?,./', n))

    if search('[0-9][0-9]', pwd) or search('[a-z][a-z]', pwd) or search('[A-Z][A-Z]', pwd) or \
            search('[A-Z][a-z]', pwd) or search('[a-z][A-Z]', pwd) or \
            search(r'[`~!@#$%^&*()_+-={}\[\]:";\'<>?,./][`~!@#$%^&*()_+-={}\[\]:";\'<>?,./]', pwd):
        pass

    else:
        print(pwd)
        break
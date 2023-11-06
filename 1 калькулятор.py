import numpy as np
x = input('x = ')
y = input('y = ')
operation = input('+; -; *; /; e^(x+y); sin(x+y); cos(x+y); x^y\n')
x, y = int(x), int(y)
try:
    match operation:
        case '+': print(x + y)
        case '-': print(x - y)
        case '*': print(x * y)
        case '/': print(x / y)
        case 'e': print(np.exp(x+y))
        case 'sin': print(np.sin(np.radians((x+y))))
        case 'cos': print(np.cos(np.radians(x+y)))
        case '^': print(x^y)
except ZeroDivisionError: 
    print('ошибка: деление на ноль')
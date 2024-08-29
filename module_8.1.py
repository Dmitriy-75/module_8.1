def add_everything_up(a,b):
    try:
        y = a+b
    except TypeError:
        y = str(a)+str(b)
    return y


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))



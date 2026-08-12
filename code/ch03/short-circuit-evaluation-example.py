def long_ass_function():
    x = 0
    for i in range(100000000):
        x = x + i
    return True


# example of short circuiting
A = True
if A and long_ass_function():
    print('The expression was true')
else:
    print('The expression was false')

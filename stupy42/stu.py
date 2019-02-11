def foo():
    a = [i**2 + 1 for i in range(5)]
    b = [(i+1.3) / (i+2.) for i in range(1, 6)]
    c = a + b
    for i, (x, y) in enumerate(zip(a, b)):
        c[i] = x * y + i
    return c

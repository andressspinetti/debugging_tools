def calc(i, n):
    j = i * n
    print 'j =', j
    if j > 0:
        print 'Positive!'
    return j


def f(n):
    for i in range(n):
        print 'i =', i
        j = calc(i, n)
    return

if __name__ == '__main__':
    f(5)
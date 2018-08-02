#!/usr/bin/env python3

if __name__ == '__main__':
    array = [1, 8, 15]
    g = (x for x in array if array.count(x) > 0)
    array = [2, 8, 22]
    p = (x for x in array if array.count(x) > 0)

    print(list(g))
    print(list(p))

    a = [''] * 3
    board = [a] * 3
    board1 = [[''] * 3 for _ in range(3)]
    print(board)
    print(board1)

    board[0][0] = 'X'
    board1[0][0] = 'X'
    print(board)
    print(board1)

    funcs = []

    for x in range(10):
        def func():
            return x
        funcs.append(func)

    print([f() for f in funcs])

    print([f(2) for f in [lambda x: x**i for i in range(10)]])

    def func(x):
        def f():
            return x
        return f

    funcs = [func(x)() for x in range(10)]

    print(funcs)
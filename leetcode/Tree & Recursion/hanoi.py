"""
Hanoi: https://zh.wikipedia.org/wiki/%E6%B1%89%E8%AF%BA%E5%A1%94
"""


def hanoi(n, a, b, c):
    """
    n: number of plates
    a: from
    b: buffer
    c: to
    """
    if n == 1:
        print(a, '-->', c)
    else:
        hanoi(n - 1, a, c, b)
        hanoi(1    , a, b, c)
        hanoi(n - 1, b, a, c)


if __name__ == '__main__':
    hanoi(5, 'A', 'B', 'C')
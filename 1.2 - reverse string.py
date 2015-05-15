# time: n, space: 1
def reverse_string(s):
    length = len(s)
    s = list(s)
    for i in range(length / 2):
        s[i], s[length - i - 1] = s[length - i - 1], s[i]
    return ''.join(s)


if __name__ == '__main__':
    import Test

    Test.test(reverse_string, [
        ('1', '1'),
        ('123', '321'),
    ])

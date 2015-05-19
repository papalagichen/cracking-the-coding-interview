# time: n^2
def remove_duplicated_characters(s):
    if s is None or len(s) < 2:
        return s
    tail = 1
    for i in range(1, len(s)):
        j = 0
        for j in range(0, tail + 1):
            if s[i] == s[j]:
                break
        if j == tail:
            s[tail] = s[i]
            tail += 1
    for i in range(tail, len(s)):
        s[i] = 0
    return s


if __name__ == '__main__':
    import Test

    Test.test(remove_duplicated_characters, [
        ('', ''),
        ([1, 1, 1, 1], [1, 0, 0, 0]),
        ([1, 1, 1, 1, 2, 2, 2, 2], [1, 2, 0, 0, 0, 0, 0, 0]),
        ([1, 2, 3, 3, 2, 1], [1, 2, 3, 0, 0, 0]),
        ([1, 2, 1, 2, 1, 2], [1, 2, 0, 0, 0, 0]),
    ])

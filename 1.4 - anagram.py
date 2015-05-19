# time: n, space: 1
def anagram(s, t):
    count = [0] * 256
    for c in s:
        count[ord(c)] += 1
    for c in t:
        count[ord(c)] -= 1
    return all(_ == 0 for _ in count)


# time: nlgn, space: 1 assume sorting algorithm is in place
def anagram2(s, t):
    return sorted(s) == sorted(t)


if __name__ == '__main__':
    import Test

    Test.test(anagram, [
        (('', ''), True),
        (('1', '1'), True),
        (('123', '321'), True),
    ])

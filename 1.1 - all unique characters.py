# time: n, space: n
def are_all_uniq(s):
    char_set = [False] * 256
    for c in s:
        if char_set[ord(c)]:
            return False
        char_set[ord(c)] = True
    return True


# time: n^2, space: 1
def are_all_uniq2(s):
    for i in range(len(s)):
        for j in range(len(s)):
            if i != j and s[i] == s[j]:
                return False
    return True


# time: nlgn, space: 1 if string is allowed to be edited
def are_all_uniq3(s):
    s = sorted(s)  # assume in place sort
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
    return True


if __name__ == '__main__':
    import Test

    Test.test((are_all_uniq, are_all_uniq2, are_all_uniq3), [
        ('1', True),
        ('11', False),
        ('12345', True),
        ('123445', False),
    ])

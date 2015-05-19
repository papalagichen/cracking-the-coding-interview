def is_rotation_string(s1, s2):
    if len(s1) == len(s2):
        return (s1 + s1).find(s2) >= 0
    return False


if __name__ == '__main__':
    import Test

    Test.test(is_rotation_string, [
        (('', ''), True),
        (('1', '1'), True),
        (('111', '111'), True),
        (('111', '1111'), False),
        (('waterbottle', 'erbottlewat'), True),
        (('123', '456'), False),
    ])

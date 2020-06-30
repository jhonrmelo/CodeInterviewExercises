"Get if two strings are oposite to each other"
def are_reverses (string_1, string_2):
    for i in range(len(string_1)):
        i_2 =  len(string_2)- i - 1
        if string_1[i]  != string_2[i_2]:
            return False
    return True

print(are_reverses("ABC", "CBA"))


"Get if an number in string is greatest than another number in string"
def largerThen(a,b):
    "in python  222 in string is bigger than 99 in string, so we can do this" 
    if len(a) > len(b):
        return True
    elif len(a) < len(b):
        return False

    for i in range(len(a)):
        if a[i] == b[i]:
            continue
        elif a[i] > b[i]:
            return True
        else:
            return False

    "the two strings are equal"
    return False

print(largerThen("112","111"))
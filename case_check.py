def case_check(string):
    upper = 0
    lower = 0
    for i in string:
        if i.isupper():
            upper = upper + 1
        elif i.islower():
            lower = lower + 1
    return upper, lower


print(case_check("Hello My Name Is Hasy"))
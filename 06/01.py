s = open('input').read()


def signal(t):
    for i in range(t, len(s) + 1):
        if len(set(s[i-t:i])) == t:
            return i


print(signal(4))
print(signal(14))

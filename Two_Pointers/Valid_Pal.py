s = "Was it a car gor a cat I saw?"
s = s.replace(" ", "")
s = s.strip("?")
s = s.lower()


def compare(l, r):
    i = 0
    while i < len(l):
        if l[i] == r[-i -1]:
            i += 1
        else:
            return False
    return True


if len(s) % 2 == 0:
    midpoint = len(s) // 2
    print(s[:midpoint], s[midpoint:])
    if compare(s[:midpoint], s[midpoint:]):
        print("its a palidrome")
    else:
        print("nope")
else:
    midpoint = len(s) // 2
    print(s[:midpoint], s[midpoint + 1:])
    if compare(s[:midpoint], s[midpoint + 1:]): # im gettin confused on how this is working fix later lmao
        print("its a palidrome")
    else:
        print("nope")

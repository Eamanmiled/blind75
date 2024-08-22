s = "zxyzxyzbhsbrstbrtbrtb"
counter = 1
for i in range(len(s)):
    lis = [s[i]]
    j = i + 1
    compare = 1
    while j < len(s):
        if s[j] in lis:
            if compare > counter:
                counter = compare
            break
        lis.append(s[j])
        j += 1
        compare += 1

print(counter)
        
        
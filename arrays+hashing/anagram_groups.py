strs = ["act", "pots", "tops", "cat", "stop", "hat"]
output = []


def anagram_check(s1, s2):
    dic_string = {}
    dic_anagram = {}
    outcome = True
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        dic_string[s1[i]] = 1 + dic_string.get(s1[i], 0)
        dic_anagram[s2[i]] = 1 + dic_anagram.get(s2[i], 0)
    if dic_string != dic_anagram:
        outcome = False
    return outcome


for i in range(len(strs)):
    j = i+1
    temp_lis = [strs[i]]
    while j < len(strs):
        contained = True
        for b in range(len(output)):
            if strs[j] in output[b]:
                contained = True
            else:
                contained = False
        if contained:
            j += 1  # see if I can remove this
        elif anagram_check(strs[i], strs[j]):
            temp_lis.append(strs[j])
            j += 1
        else:
            j += 1
    output.append(temp_lis)
print(output)

# jesus its late but i made some bollocks of this code kill me


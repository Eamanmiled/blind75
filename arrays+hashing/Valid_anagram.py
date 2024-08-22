string = "racecar"
anagram = "      car    race     "
string = string.replace(" ", "")
stripped = anagram.replace(" ", "")

dic_string = {}
dic_anagram = {}
outcome = True
if len(string) != len(stripped):
    outcome = False
    for i in range(len(string)):
        dic_string[string[i]] = 1 + dic_string.get(string[i], 0)
        dic_anagram[anagram[i]] = 1 + dic_anagram.get(anagram[i], 0)
    if dic_string != dic_anagram:
        outcome = False
print(outcome)
        
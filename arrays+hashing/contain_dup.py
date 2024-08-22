lis = [1,2,4,5,6]
dup_lis = []
outcome = True
for i in range(len(lis)):
    if lis[i] not in dup_lis:
        dup_lis.append(lis[i])
    else:
        outcome = False
        break
print(outcome)

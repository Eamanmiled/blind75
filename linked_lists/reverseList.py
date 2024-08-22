head = [0,1,2,3]
tails =[]

counter = len(head) - 1
while not counter < 0:
    tails.append(head[counter])
    counter -= 1
print(tails)
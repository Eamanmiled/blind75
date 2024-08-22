nums = [-1, 0, 1, 2, -1, -4]
target = 0

output = []
for loop1 in range(len(nums)):
    loop2 = loop1 + 1
    while loop2 < len(nums):
        loop3 = loop2 + 1
        while loop3 < len(nums):
            if nums[loop1] + nums[loop2] + nums[loop3] == target:
                output.append((nums[loop1], nums[loop2], nums[loop3]))
            loop3 += 1
        loop2 += 1

for i in range(len(output)-1):
    check = output[i]
    compare = output[i + 1]
    if check[0] and check[1] and check[2] in compare:
        output.pop(i + 1)

print(output)

nums = [0, 3, 4, 5, 6, 7]
target = 7
index_ans=[]

for i in range(len(nums)):
    j = i+1
    while j < len(nums):
        if nums[i] + nums[j] == target:
            index_ans.append((i,j))
        j += 1
print(index_ans)

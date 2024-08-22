nums = [3, 4, 5, 6, 1, 2]
L = 0
R = len(nums) - 1
midpoint = len(nums) // 2


while True:
    if R - L == 2:
        if nums[L] < nums[R] and nums[L] < nums[R-1]:
            print(nums[L], "is smallest @ index", L)
            break
        elif nums[R] < nums[L] and nums[R] < nums[R-1]:
            print(nums[R], "is smallest @ index", R)
            break
        else:
            print(nums[R-1], "is the smallest @ index", R-1)
            break
    if nums[L] < nums[R]:
        R = midpoint
    else:
        L = midpoint
    midpoint = L + R // 2



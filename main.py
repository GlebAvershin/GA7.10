# sorted choice
nums = [5,7,8,2,3,1,4,9,6]
for i in range(len(nums)):
    low = i
    for j in range(i+1, len(nums)):
        if nums[j] < nums[low]:
            low = j
    nums[i], nums[low] = nums[low], nums[i]
print(nums)

def R(n):
    if n == 1:
        return n
    if n >= 3:
        return F(n + 1)
print(R(3))
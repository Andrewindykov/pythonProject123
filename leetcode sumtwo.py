def twoSum(nums,target):
    se=dict()
    for i in range(len(nums)):
        se[nums[i]]=i
    for i in range(len(nums)):
        diff=target-nums[i]
        if diff in se.keys() and i != se[diff]:
            return [i,se[diff]]
    print(se)
    return 777
A=[3,2,4]
print(A)
print(twoSum (A,6))
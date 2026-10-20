class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product, zeroCount = 1,0
        for num in nums:
            if num != 0:
                product *= num
            else:
                zeroCount += 1
        if zeroCount > 1:
            return [0] * len(nums)
        
        result = [0] * len(nums)
        for i,c in enumerate(nums):
            if zeroCount != 0:
                result[i] = 0 if c else product
            else:
                result[i] = product // c
        return result

# ONE ZERO CASE
#[-1,0,1,2,3]
# product = -1 * 1 * 2 * 3 = -6
# zeroCount = 1
# result = [0,0,0,0,0]
# (0,-1) (1,0) (2,1) (3,2) (4,3)
# result = [0, -6, 0, 0, 0]

# NO ZEROS CASE
# [1,2,4,6]
# product = 48
# zeroCount = 0
# result = [0,0,0,0]
# (0,1) (1,2) (2,4) (3,6)
# result = [48, 24, 12, 8]

# TWO ZEROS CASE
#[-1,0,0,2,3]
#product = -1 * 2 * 3 = -6
#zeroCount = 2
#result = [0,0,0,0,0] 
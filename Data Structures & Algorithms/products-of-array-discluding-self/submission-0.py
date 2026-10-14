class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        p = 1
        for i in range(1, len(nums)):
            p *= nums[i - 1]
            res[i] *= p
            
        p = 1
        for j in range(len(nums) - 2, -1, -1):
            p *= nums[j + 1]
            res[j] *= p
        
        return(res)
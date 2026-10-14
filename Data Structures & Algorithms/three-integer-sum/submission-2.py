class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    res.append([nums[i], nums[j], nums[k]])
                
                if total < 0:
                    j += 1
                else:
                    k -= 1

        result = list(set(tuple(x) for x in res))
        result = [list(x) for x in result]
        return result
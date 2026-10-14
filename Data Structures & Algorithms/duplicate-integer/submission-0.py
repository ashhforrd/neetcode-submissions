class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        number = {}

        for n in nums:
            number[n] = number.get(n, 0) + 1
        
        return any(v > 1 for v in number.values())
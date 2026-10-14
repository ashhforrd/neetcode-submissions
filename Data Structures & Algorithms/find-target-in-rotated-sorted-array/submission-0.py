class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s = set(nums)

        return nums.index(target) if target in s else -1
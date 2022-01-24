class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = []

        if target not in nums:
            return [-1, -1]

        first_idx = nums.index(target)
        hold = first_idx

        for i in range(first_idx + 1 , len(nums)):

            if nums[i]!=target:
                break
                
            hold = i

        return [first_idx, hold]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_seen = {}
        for i in range(len(nums)):
            if target - nums[i] in nums_seen:
                # check if the matching number exists to satisfy the target
                match = nums_seen.get(target - nums[i])
                if match is not None:
                    return [match, i]
            if nums[i] not in nums_seen:
                nums_seen[nums[i]] = i
        return None
            



        
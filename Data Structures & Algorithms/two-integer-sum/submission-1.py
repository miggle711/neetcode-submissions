class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_seen = {}
        for i in range(len(nums)):
            # check if a matching number exists to satisfy the equation:
            #     - match = target - nums[i]
            if target - nums[i] in nums_seen:
                match = nums_seen.get(target - nums[i])
                if match is not None:
                    return [match, i]
            # keep track of the existence of a number and its last seen id
            if nums[i] not in nums_seen:
                nums_seen[nums[i]] = i
        return None
            



        
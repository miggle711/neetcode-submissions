class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_map = {}
        for i in range(len(nums)):
            if nums[i] not in num_map:
                num_map[nums[i]] = 1
            else:
                num_map[nums[i]] += 1

        res = 0
        prev_val = -1
        for i in range(len(num_map.items())):
            if num_map.get(i) is not None and i - prev_val == 1:
                res += 1
            prev_val = i
        return res
        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_seq = 0 
        i = 0
        while i < len(nums):
            if nums[i] - 1 not in num_set:
                # nums[i] is the start of a consecutive sequence
                len_consec = 1
                curr_num = nums[i]
                # traverse the sequence and get its length
                while curr_num + 1 in num_set:
                    len_consec += 1
                    curr_num += 1
                if len_consec > longest_seq:
                     longest_seq = len_consec
            i += 1
        return longest_seq
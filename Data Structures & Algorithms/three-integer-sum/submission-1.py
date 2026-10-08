class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # we sort the array to make it easier to avoid duplicates and use two pointers
        nums.sort()
        threesome = []
        for i in range(len(nums)):
            # we skip the same element to avoid duplicates in the result
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = len(nums) - 1

            # we use two pointers to find pairs that sum up to the negative of the current number
            while l < r:
                if nums[l] + nums[r] == -nums[i]:
                    threesome.append([nums[i],nums[l],nums[r]])
                    # we skip the same elements to avoid duplicates in the result
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                # if the sum of the two pointers is less than the negative of the current number, we move the left pointer to the right to increase the sum
                elif nums[l] + nums[r] < -nums[i]:
                    l += 1
                # if the sum of the two pointers is greater than the negative of the current number, we move the right pointer to the left to decrease the sum
                else:
                    r -= 1
        return threesome

        
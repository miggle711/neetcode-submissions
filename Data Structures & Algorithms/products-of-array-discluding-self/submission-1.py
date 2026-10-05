class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        res[0] = 1

        # Get prefix product
        prefix_product = 1
        for i in range(1, len(nums)):
            prefix_product *= nums[i - 1]
            res[i] = prefix_product

        # Get suffix product
        suffix_product = 1
        # res = [0] * len(nums)
        # res[-1] = 1
        for j in range(len(nums) - 2, -1, -1):
            suffix_product *= nums[j + 1]
            res[j] *= suffix_product

        return res
        



        
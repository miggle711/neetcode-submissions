class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        The product of all elems except nums[i] can we expressed as:
            - (a) the product of all elems from nums[0] to nums[i -1] MULTIPLIED BY
            - (b) the product of al elems from nums[i + 1] to nums[n -1] (n = len(nums))

        - the answer for this problem is then simply the 
          element-wise product of (a) and (b) 
        - i.e. taking the combined product of all elems left of nums[i] TIMES
          the combined product of all elems right of nums[i]
        """
        res = [0] * len(nums)

        # we set the prefix to be 1 for the first elem to prevent muliplication by 0
        # and any number times 1 is still itself
        res[0] = 1 

        # Get prefix product
        product = 1
        # start from the left 
        for i in range(1, len(nums)):
            # get the combined product of all elems left of nums[i]
            product *= nums[i - 1] 
            res[i] = product

        # Get suffix product
        product = 1
         # start from the right
        for j in range(len(nums) - 2, -1, -1):
            # get the combined product of all elems right of nums[i]
            product *= nums[j + 1]
            res[j] *= product

        return res
        



        
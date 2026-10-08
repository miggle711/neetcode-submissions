class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        largest_area = 0
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            if area > largest_area:
                largest_area = area
                print(area)
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l +=1
                r -= 1
        return largest_area
            
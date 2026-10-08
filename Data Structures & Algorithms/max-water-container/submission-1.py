class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        largest_area = 0
        while l < r:
            # the shorter column bounds the area
            area = (r - l) * min(heights[l], heights[r])
            if area > largest_area:
                largest_area = area
            
            # if the col is the shortest, move it to try to search for taller cols
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l +=1
                r -= 1
        return largest_area
            
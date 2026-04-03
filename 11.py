class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        max_water = 0

        # amount of water = a*b
        while i < j:
            water_amount = min(height[i], height[j]) * (j-i)
            if water_amount > max_water:
                max_water = water_amount
            if height[i] < height[j]: # increment the lower end
                i += 1
            else:
                j -= 1

        return max_water
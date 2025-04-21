class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        min_sum = 0
        max_sum = 0 
        current = 0

        for diff in differences:
            current += diff 
            min_sum = min(min_sum, current)
            max_sum = max(max_sum, current)

        min_x = lower - min_sum
        max_x = upper - max_sum 

        return max(0, max_x - min_x+1)


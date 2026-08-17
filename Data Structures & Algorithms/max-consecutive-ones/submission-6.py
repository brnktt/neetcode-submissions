class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        times = 0
        max_times = 0
        prev = 0
        for num in nums:
            if num == 1:
                prev = num
                times += 1
            else:
                if times > max_times:
                    max_times = times
                times = 0
                prev = 0
        if max_times > times:
            return max_times
        else:
            return times
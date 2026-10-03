class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top = {}

        for n in nums:
            top[n] = top.get(n, 0) + 1

        sorted_elements = sorted(top.keys(), key = lambda x: top[x], reverse=True)
        return sorted_elements[:k]
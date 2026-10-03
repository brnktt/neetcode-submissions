class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for n in nums:
            frequency[n] = frequency.get(n, 0) + 1
        
        sorted_elements = sorted(frequency.keys(), key=lambda x: frequency[x], reverse=True)
        return sorted_elements[:k]
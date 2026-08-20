class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tmp = []
        for num in nums: 
            if num != val:
                tmp.append(num)
        k = len(tmp)
        for i in range(k):
            nums[i] = tmp[i]
        return k
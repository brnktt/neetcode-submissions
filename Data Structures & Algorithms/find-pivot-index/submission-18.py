class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix, postfix = [], []
        pre_total, post_total = 0, 0

        for n in nums:
            pre_total += n
            prefix.append(pre_total)

        for i in range(len(nums) - 1, -1, -1):
            post_total += nums[i]
            postfix.append(post_total)
        postfix.reverse()

        for i in range(len(nums)):
            left_sum = prefix[i - 1] if i > 0 else 0
            right_sum = postfix[i + 1] if i < len(nums) - 1 else 0
            if left_sum == right_sum:
                return i
        return -1
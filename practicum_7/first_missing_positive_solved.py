class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_pos_n = None
        max_n = 0
        for i in range(len(nums)):
            n = nums[i]
            if n > max_n:
                max_n = n
            if min_pos_n is None and n > 0:
                min_pos_n = n
            if 0 < n < min_pos_n:
                min_pos_n = n
            nums[i] = 1 if n < 0 else n + 1
        if min_pos_n != 1:
            return 1
        for i in range(len(nums)):
            access_i = abs(nums[i]) - 2
            if 0 <= access_i < len(nums):
                nums[access_i] = -1 * abs(nums[access_i])
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        return max_n + 1


if __name__ == "__main__":
    # Let's solve First Missing Positive problem:
    # https://leetcode.com/problems/first-missing-positive
    nums = [0, 1, 2]
    n = Solution().firstMissingPositive(nums)
    nums = [2, 1]
    n = Solution().firstMissingPositive(nums)
    nums = [1, 2, 0]
    n = Solution().firstMissingPositive(nums)
    nums = [3, 4, -1, 1]
    n = Solution().firstMissingPositive(nums)
    nums = [7, 8, 9, 11, 12]
    n = Solution().firstMissingPositive(nums)

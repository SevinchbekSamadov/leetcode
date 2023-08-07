class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if i + 1 >= len(nums):
                i -= 1
            if nums[i] < nums[i + 1]:
                count += 1
        return count

son_1 = Solution()
print(son_1.findNumberOfLIS([1,2,3,4,2,3]))
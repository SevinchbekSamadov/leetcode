class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        nums = sorted(nums)
        for i in range(0,len(nums),2):
            if i + 1 >= len(nums):
                return nums[i]
            if nums[i] != nums[i + 1]:
                return nums[i]

a = Solution()
print(a.singleNumber(nums = [2,2,1]))
#1
print(a.singleNumber(nums = [4,1,2,1,2]))
#4
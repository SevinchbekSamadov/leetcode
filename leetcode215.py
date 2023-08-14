class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums = sorted(nums)
        return nums[len(nums) - k ]

a = Solution()
print(a.findKthLargest(nums = [3,2,1,5,6,4], k = 2))
Output: 5
class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        # a = []
        # for i in range(n):
        #     a.append(nums[i])
        #     a.append(nums[n+i])
        # return a
        nums[::2],nums[1::2]=nums[:n],nums[n:]
        return nums
a = Solution()
print(a.shuffle(nums = [2,5,1,3,4,7], n = 3))
print(a.shuffle(nums = [1,2,3,4,4,3,2,1], n = 4))


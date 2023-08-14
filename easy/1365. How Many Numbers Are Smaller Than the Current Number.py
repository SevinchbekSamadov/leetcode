class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        def getResult():
            for i in nums:
                count = 0
                for j in nums:
                    if i > j:
                        count += 1
                yield count
        return list(getResult())
        # arr = []
        # for i in nums:
        #     count  = 0
        #     for j in nums:
        #         if i > j:
        #             count += 1
        #     arr.append(count)
        # return arr
        
a = Solution()
print(a.smallerNumbersThanCurrent(nums = [8,1,2,2,3]))
Output: [4,0,1,1,3]
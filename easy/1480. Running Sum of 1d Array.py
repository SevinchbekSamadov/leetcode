from functools import reduce
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        def getResult():
            for i in range(len(nums)):
                yield reduce(lambda x,y : x + y,nums[:i+1])
        return list(getResult())
        # a = []
        # for i in range(len(nums)):
        #     a.append(reduce(lambda x,y : x + y,nums[:i+1]))
        # return a

a = Solution()
print(a.runningSum(nums = [1,2,3,4]))
Output: [1,3,6,10]
print(a.runningSum(nums = [1,1,1,1]))
        # return [sum(nums[:i + 1]) for i in range(len(nums))]
        # def getResult():
        #     for i in range(len(nums)):
        #         yield sum(nums[:i + 1])
        # return list(getResult())
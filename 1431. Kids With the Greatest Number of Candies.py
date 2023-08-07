class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        b = max(candies)
        # a = []
        # for i in candies:
        #     if i + extraCandies >= b:
        #         a.append(True)
        #     else:
        #         a.append(False)
        # return a
        def getResult():
            for i  in candies:
                yield i + extraCandies >= b
        return list(getResult())



            

a = Solution()
print(a.kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3))
# Output: [true,true,true,false,true]
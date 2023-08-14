class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        son = 0
        a = len(digits)
        for i in digits:
            son += i * (10 ** (a -1))
            a -= 1
        son += 1
        javob = []
        for i in range(len(str(son))):
            javob.append(son % 10)
            son //= 10
        return list(reversed(javob))
     
        # return list(map(int,list(str(son))))
    
a = Solution()
print(a.plusOne(digits = [1,2,3]))
Output: [1,2,4]
    
    
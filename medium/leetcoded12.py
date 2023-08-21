class Solution:
    def intToRoman(self, num: int) -> str:
        nums = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        roman = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
        a = len(nums)
        l = ''
        for i in range(len(nums) - 1,-1,-1):
            if num > nums[i]:
                j = num // nums[i]
                num = num % nums[i]
                l += j * roman[i]
        return l

        
0
a = Solution()
print(a.intToRoman( num = 3))
# Output: "III"
print(a.intToRoman( num = 58))
print(a.intToRoman( num = 1994))
#"MCMXCIV"
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
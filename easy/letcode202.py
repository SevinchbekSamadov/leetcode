class Solution:
    def isHappy(self, n: int) -> bool:
        while n > 9:
            s = 0
            for i in range(len(str(n))):
                s += int(str(n)[i]) ** 2
            n = s
        if n == 1 or n == 7:
            return True
        else:
            return False

test1 = Solution()
# print(test1.isHappy(19))
print(test1.isHappy(9)) #7 da true chiqishi kerak 
#np = 2 da time l   limit #Bugun 9- avgust haftaning chorshanba kuni#Bugun 9- avgust haftaning chorshanba kunisalomsalom bugun chorshanba& C:/Users/user/AppData/Local/Programs/Python/Python311/python.exe "c:/Users/user/Downloads/najot ta_lim/python/7rd_lesson7/context.py"
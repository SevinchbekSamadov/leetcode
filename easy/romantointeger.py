class Solution:
    def romanToInt(self, s: str) -> int:
        rome_number = ['I','V','X','L','C','D','M']
        arab_number = [1,5,10,50,100,500,1000]
        summ = 0
        for i in range(len(s)):
            if s[i] in rome_number:
                indeks = rome_number.index(s[i])
                summ += arab_number[indeks]
                if i + 1 == len(s):
                    i = i - 1
                if indeks < rome_number.index(s[i + 1]):
                    summ -= 2 * arab_number[indeks]
        return summ         
a = Solution()
print(a.romanToInt("III"))
print(a.romanToInt("LVIII"))
print(a.romanToInt("MCMXCIV"))



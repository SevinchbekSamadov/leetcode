class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s[::-1])
        a = []
        b =''
        for j in s:
            # print(j)
            if  j != ' ':
                b += j
                print(b)
            else:
                a.append(b)
                b = ''
        a.append(b)
        def getResult():
            for i in range(len(a)-1,-1,-1):
                
                yield a[i]
        return ' '.join(getResult())
    #split ni ham ishlatrish kerak spliut ajratishda ishlatiladi  
a = Solution()
print(a.reverseWords(s = "Let's take LeetCode contest"))
"s'teL ekat edoCteeL tsetnoc"
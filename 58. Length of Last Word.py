class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        print(set(s))
        b = list(s[::-1])
        # if s in ascii:
        #     return 1
        count = 0
        for i in range(len(s)):
            if b[i] ==" ":
                continue
            else:
                count += 1
                if b[i + 1] == " ":
                    break
        return count


    
a = Solution()
print(a.lengthOfLastWord(s = "Hello World"))
#5
print(a.lengthOfLastWord(s = "   fly me   to   the moon  "))
#4
print(a.lengthOfLastWord( s = "luffy is still joyboy"))
#6


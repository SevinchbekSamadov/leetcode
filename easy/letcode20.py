class Solution:
    def isValid(self, s: str) -> bool:
        open_brack = ['(','[','{']
        close_brack = [')',']','}']
        x = False
        k = 1
        if len(s) % 2 == 1:
            return False
        for i in s:
            if i in close_brack:
                return False
            if i in open_brack:
                k = open_brack.index(i)
                l = s.index(i)
                b = s.index(close_brack[k])
            if (b - l) % 2 == 0 or b == l + 1:
                return True
         
        # for i in range(3):
        #     if open_brack[i] in s:
        #         l = s.index(open_brack[i])
        #         if close_brack[i] in s:
        #             k = s.index(close_brack[i])
        #         else:
        #             x = False
        #     if (k - l ) % 2 == 0 or k == l + 1:
        #        x = True
        #     else:
        #         break
        return x
         


        

test = Solution()
print(test.isValid("()"))
print(test.isValid("()[]{}"))
print(test.isValid("(]"))
print(test.isValid("(([]))"))
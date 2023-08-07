class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        c = (operations)
        o = 0
        for i in range(len(operations)):
            if i == len(operations) - 1:
                break
            l = next(c)
            match l:
                case "--X" | "X--":
                    o -= 1
                case "X++" | "X++":
                    o += 1
        return o


                        
                
            

        pass 

a = Solution()
print(a.finalValueAfterOperations(operations = ["--X","X++","X++"]))
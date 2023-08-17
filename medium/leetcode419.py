class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        count  = 0
        for i in board:
            for j in range(len(i)):
                if i[j] == "X":
                    count += 1
                    if j + 1 != len(i):
                        if i[j + 1] == "X":
                            count -= 1
        for k in range(len(board) - 1):
            for l in range(len(board[k])):
                if (board[k])[l] == "X" and (board[k + 1])[l] == "X":
                    count -= 1

        return count
        
                

a = Solution()
print(a.countBattleships(board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]))
#2
# ["X",".",".","X"]
# [".",".",".","X"]
# [".",".",".","X"]  kemalar sonini topish kerak  har bir kema boshqasidan bitta "." ga farq qiladi.
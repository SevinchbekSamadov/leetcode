class Solution:
    def capitalizeTitle(self, title: str) -> str:
        b = title.split(' ')
        def getResult():
            for i in range(len((b))):
                if len(b[i]) > 2:
                    b[i] = b[i].title()
                else:
                    b[i] = b[i].lower()
                yield b[i]
        return ' '.join(getResult())

a = Solution()
print(a.capitalizeTitle(title = "sfdugayfg ASaytsduuiaudv hyasdysYGY TH hasudgfu GYShuhu"))
"Capitalize The Title"
class Solution:

    def encode(self, strs: List[str]) -> str:
        retval = ""
        for s in strs:
            retval += str(len(s))
            retval += "#"
            retval += s
        return retval

    def decode(self, s: str) -> List[str]:
        retval = []
        writeword = ""
        num = True
        length = ""
        word = 0
        while word < len(s):
            # print(word)
            # print(s[word])
            if num == True and s[word] != "#":
                length += s[word]
            else:
                if int(length) == 0:
                    retval.append("")
                else:
                    if num == True:
                        num = False
                        word += 1
                        lengthnum = int(length)
                    if lengthnum != 0:
                        writeword += s[word]
                        lengthnum -= 1
                    if lengthnum == 0:
                        retval.append(writeword)
                        num = True
                        writeword = ""
                        lengthnum = 0
                        length = ""
            word += 1
        return retval

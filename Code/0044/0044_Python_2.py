class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        N1 = len(s)  # 字符串长度
        N2 = len(p)  # 模式长度

        # 匹配最后一个*之后的内容是否匹配
        while N1 > 0 and N2 > 0 and p[N2 - 1] != "*":
            if p[N2 - 1] == "?" or p[N2 - 1] == s[N1 - 1]:
                N1 -= 1
                N2 -= 1
            else:
                return False

        # 处理模式已空的情况
        if N2 == 0:
            return N1 == 0

        # 匹配最后一个*之前的内容是否匹配
        i1 = i2 = 0
        r1 = r2 = -1
        while i1 < N1 and i2 < N2:
            if p[i2] == "*":
                i2 += 1
                r1 = i1
                r2 = i2
            elif p[i2] == "?" or p[i2] == s[i1]:
                i1 += 1
                i2 += 1
            elif r1 != -1:
                r1 += 1
                i1 = r1
                i2 = r2
            else:
                return False
            
        return all(i == "*" for i in p[i2:N2])


if __name__ == "__main__":
    print(Solution().isMatch(s="aa", p="a"))  # False
    print(Solution().isMatch(s="aa", p="*"))  # True
    print(Solution().isMatch(s="cb", p="?a"))  # False
    print(Solution().isMatch(s="adceb", p="*a*b"))  # True
    print(Solution().isMatch(s="acdcb", p="a*c?b"))  # False
    print(Solution().isMatch(s="", p="a"))  # False
    print(Solution().isMatch(s="", p="?"))  # False
    print(Solution().isMatch(s="aaab", p="b***"))  # False

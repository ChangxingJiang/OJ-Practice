class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        N1, N2 = len(s), len(t)

        # 处理特殊情况
        if N1 != N2:
            return False

        # 统计k中可以处理各种切换数量的次数
        a, b = divmod(k, 26)
        count = [a + 1] * b + [a] * (26 - b)

        # 统计将s变为t所需要的切换次数
        for i in range(N1):
            if s[i] != t[i]:
                c1, c2 = ord(s[i]), ord(t[i])
                diff = (c2 + 26 - c1) % 26
                if count[diff - 1] > 0:
                    count[diff - 1] -= 1
                else:
                    return False

        return True


if __name__ == "__main__":
    print(Solution().canConvertString(s="input", t="ouput", k=9))  # True
    print(Solution().canConvertString(s="abc", t="bcd", k=10))  # False
    print(Solution().canConvertString(s="aab", t="bbb", k=27))  # True

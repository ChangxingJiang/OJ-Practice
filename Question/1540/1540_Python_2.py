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
        for s_ch, t_ch in zip(s, t):
            diff = (ord(t_ch) - ord(s_ch)) % 26 - 1
            if diff >= 0:
                if count[diff] > 0:
                    count[diff] -= 1
                else:
                    return False

        return True


if __name__ == "__main__":
    print(Solution().canConvertString(s="input", t="ouput", k=9))  # True
    print(Solution().canConvertString(s="abc", t="bcd", k=10))  # False
    print(Solution().canConvertString(s="aab", t="bbb", k=27))  # True

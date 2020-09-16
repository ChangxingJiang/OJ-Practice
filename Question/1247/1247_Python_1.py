class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        N = len(s1)

        # 统计两字符串中不同的情况
        count1 = 0
        count2 = 0
        for i in range(N):
            ch1 = s1[i]
            ch2 = s2[i]
            if ch1 == "x" and ch2 == "y":
                count1 += 1
            elif ch1 == "y" and ch2 == "x":
                count2 += 1

        a1, b1 = divmod(count1, 2)
        a2, b2 = divmod(count2, 2)

        # 判断两字符串是否可交换生成
        if b1 + b2 != 1:
            return a1 + a2 + b1 + b2
        else:
            return -1


if __name__ == "__main__":
    print(Solution().minimumSwap(s1="xx", s2="yy"))  # 1
    print(Solution().minimumSwap(s1="xy", s2="yx"))  # 2
    print(Solution().minimumSwap(s1="xx", s2="xy"))  # -1
    print(Solution().minimumSwap(s1="xxyyxyxyxx", s2="xyyxyxxxyx"))  # 4
    print(Solution().minimumSwap(s1="xxxxyyyy", s2="yyyyxyyx"))  # 3

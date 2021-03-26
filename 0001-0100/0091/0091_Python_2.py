class Solution:
    def numDecodings(self, s: str) -> int:
        stats = []
        last = None
        for ch in s[::-1]:
            if ch == "0":
                stats.append(0)
                last = int(ch)
            elif not stats:  # 处理第一个元素的情况
                stats.append(1)
                last = int(ch)
            elif len(stats) == 1:  # 处理第二个元素的情况
                n = int(ch)
                if 10 * n + last <= 26:
                    stats.append(1 + stats[-1])
                else:
                    stats.append(stats[-1])
                last = n
            else:
                n = int(ch)
                if 10 * n + last <= 26:
                    stats.append(stats[-2] + stats[-1])
                else:
                    stats.append(stats[-1])
                last = n
        return stats[-1]


if __name__ == "__main__":
    print(Solution().numDecodings("12"))  # 2
    print(Solution().numDecodings("226"))  # 3
    print(Solution().numDecodings("0"))  # 0
    print(Solution().numDecodings("10"))  # 1
    print(Solution().numDecodings("230"))  # 0

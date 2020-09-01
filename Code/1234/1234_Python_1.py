class Solution:
    def balancedString(self, s: str) -> int:
        N = len(s)
        n = N // 4

        # 统计各个字母的数量
        q = s.count("Q")
        w = s.count("W")
        e = s.count("E")
        r = s.count("R")

        # 计算各个字母需要被替换为其他字母的数量
        q = (q - n) if q > n else 0
        w = (w - n) if w > n else 0
        e = (e - n) if e > n else 0
        r = (r - n) if r > n else 0
        num = q + w + e + r
        if num == 0:
            return 0

        # 滑动窗口计算最短替换字符串
        left = 0
        right = 0
        ans = N
        while right < N:
            ch = s[right]
            if ch == "Q":
                if q > 0:
                    num -= 1
                q -= 1
            elif ch == "W":
                if w > 0:
                    num -= 1
                w -= 1
            elif ch == "E":
                if e > 0:
                    num -= 1
                e -= 1
            else:
                if r > 0:
                    num -= 1
                r -= 1
            right += 1

            if num == 0:
                while num <= 0 and left < right:
                    ch = s[left]
                    if ch == "Q":
                        q += 1
                        if q > 0:
                            num += 1
                    elif ch == "W":
                        w += 1
                        if w > 0:
                            num += 1
                    elif ch == "E":
                        e += 1
                        if e > 0:
                            num += 1
                    else:
                        r += 1
                        if r > 0:
                            num += 1
                    left += 1
                ans = min(ans, right - left + 1)
        return ans


if __name__ == "__main__":
    print(Solution().balancedString(s="QWER"))  # 0
    print(Solution().balancedString(s="QQWE"))  # 1
    print(Solution().balancedString(s="QQQW"))  # 2
    print(Solution().balancedString(s="QQQQ"))  # 3
    print(Solution().balancedString(s="WWEQERQWQWWRWWERQWEQ"))  # 4

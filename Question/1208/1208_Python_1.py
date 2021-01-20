class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        size = len(s)

        lst = []
        for i in range(size):
            lst.append(abs(ord(s[i]) - ord(t[i])))

        ans = 0

        left = 0
        cost = 0
        for right in range(size):
            cost += lst[right]
            right += 1
            while cost > maxCost:
                cost -= lst[left]
                left += 1
            ans = max(ans, right - left)

        return ans


if __name__ == "__main__":
    print(Solution().equalSubstring(s="abcd", t="bcdf", maxCost=3))  # 3
    print(Solution().equalSubstring(s="abcd", t="cdef", maxCost=3))  # 1
    print(Solution().equalSubstring(s="abcd", t="acde", maxCost=0))  # 1

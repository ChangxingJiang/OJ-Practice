class Solution:
    def countLetters(self, S: str) -> int:
        now = ""
        num = 0
        ans = 0
        for ch in S:
            if ch != now:
                ans += (1 + num) * num // 2
                now = ch
                num = 1
            else:
                num += 1
        ans += (1 + num) * num // 2
        return ans


if __name__ == "__main__":
    print(Solution().countLetters("aaaba"))  # 8
    print(Solution().countLetters("aaaaaaaaaa"))  # 55

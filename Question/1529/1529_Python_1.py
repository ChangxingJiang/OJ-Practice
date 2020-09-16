class Solution:
    def minFlips(self, target: str) -> int:
        ans = 0
        now = "0"
        for ch in target:
            if ch != now:
                now = ch
                ans += 1
        return ans


if __name__ == "__main__":
    print(Solution().minFlips(target="10111"))  # 3
    print(Solution().minFlips(target="101"))  # 3
    print(Solution().minFlips(target="00000"))  # 0
    print(Solution().minFlips(target="001011101"))  # 5

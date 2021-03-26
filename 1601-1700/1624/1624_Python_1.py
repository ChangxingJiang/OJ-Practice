class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1
        dic = {}
        for i, ch in enumerate(s):
            if ch in dic:
                ans = max(ans, i - dic[ch] - 1)
            else:
                dic[ch] = i
        return ans


if __name__ == "__main__":
    print(Solution().maxLengthBetweenEqualCharacters("aa"))  # 0
    print(Solution().maxLengthBetweenEqualCharacters("abca"))  # 2
    print(Solution().maxLengthBetweenEqualCharacters("cbzxy"))  # -1
    print(Solution().maxLengthBetweenEqualCharacters("cabbac"))  # 4
    print(Solution().maxLengthBetweenEqualCharacters("mgntdygtxrvxjnwksqhxuxtrv"))  # 18

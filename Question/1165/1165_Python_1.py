class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        dic = {ch: i for i, ch in enumerate(keyboard)}
        ans = 0
        now = 0
        for ch in word:
            ans += abs(dic[ch] - now)
            now = dic[ch]
        return ans


if __name__ == "__main__":
    # 4
    print(Solution().calculateTime(keyboard="abcdefghijklmnopqrstuvwxyz", word="cba"))

    # 73
    print(Solution().calculateTime(keyboard="pqrstuvwxyzabcdefghijklmno", word="leetcode"))

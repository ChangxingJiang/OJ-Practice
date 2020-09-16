class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        hashmap = {0: -1}
        now = 0  # 当前状态
        ans = 0
        for i, ch in enumerate(s):
            if ch in {"a", "e", "i", "o", "u"}:
                # 判断当前状态的最长子串
                if now in hashmap:
                    ans = max(ans, i - hashmap[now] - 1)

                # 更新当前状态
                if ch == "a":
                    now ^= 16
                elif ch == "e":
                    now ^= 8
                elif ch == "i":
                    now ^= 4
                elif ch == "o":
                    now ^= 2
                elif ch == "u":
                    now ^= 1

                # 记录新状态的位置
                if now not in hashmap:
                    hashmap[now] = i
        if now in hashmap:
            ans = max(ans, len(s) - hashmap[now] - 1)
        return ans


if __name__ == "__main__":
    print(Solution().findTheLongestSubstring(s="eleetminicoworoep"))  # 13
    print(Solution().findTheLongestSubstring(s="leetcodeisgreat"))  # 5
    print(Solution().findTheLongestSubstring(s="bcbcbc"))  # 6

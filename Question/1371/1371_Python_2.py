class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        now = [True, True, True, True, True]  # 当前状态
        hashmap = {tuple(now): -1}
        ans = 0
        for i, ch in enumerate(s):
            # 更新当前状态
            if ch == "a":
                now[0] = not now[0]
            elif ch == "e":
                now[1] = not now[1]
            elif ch == "i":
                now[2] = not now[2]
            elif ch == "o":
                now[3] = not now[3]
            elif ch == "u":
                now[4] = not now[4]

            # 判断当前状态的最长子串
            this = tuple(now)
            if this in hashmap:
                ans = max(ans, i - hashmap[this])
            else:
                hashmap[this] = i
        return ans


if __name__ == "__main__":
    print(Solution().findTheLongestSubstring(s="eleetminicoworoep"))  # 13
    print(Solution().findTheLongestSubstring(s="leetcodeisgreat"))  # 5
    print(Solution().findTheLongestSubstring(s="bcbcbc"))  # 6

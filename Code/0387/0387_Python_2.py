class Solution:
    def firstUniqChar(self, s: str) -> int:
        once = []
        repeat = []
        for c in s:
            if c not in repeat:
                if c not in once:
                    once.append(c)
                else:
                    once.remove(c)
                    repeat.append(c)
        if len(once) > 0:
            return s.index(once[0])
        else:
            return -1


if __name__ == "__main__":
    print(Solution().firstUniqChar("aabb"))  # -1
    print(Solution().firstUniqChar("leetcode"))  # 0
    print(Solution().firstUniqChar("loveleetcode"))  # 2

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        repeat = []
        for i in range(len(s)):
            c = s[i]
            if c not in repeat:
                if c not in hashmap:
                    hashmap[c] = i
                else:
                    del hashmap[c]
                    repeat.append(c)
        if len(hashmap.values()) > 0:
            return min(hashmap.values())
        else:
            return -1


if __name__ == "__main__":
    print(Solution().firstUniqChar("aabb"))  # -1
    print(Solution().firstUniqChar("leetcode"))  # 0
    print(Solution().firstUniqChar("loveleetcode"))  # 2

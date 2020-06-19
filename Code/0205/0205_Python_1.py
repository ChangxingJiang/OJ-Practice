class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        size_s = len(s)
        size_t = len(t)
        if size_s != size_t:
            return False

        hashmap_s = {}
        for i in range(size_s):
            c = s[i]
            if c not in hashmap_s:
                if t[i] not in hashmap_s.values():
                    hashmap_s[c] = t[i]
                else:
                    return False
            if t[i] != hashmap_s[c]:
                return False

        return True


if __name__ == "__main__":
    print(Solution().isIsomorphic("egg", "add"))  # True
    print(Solution().isIsomorphic("foo", "bar"))  # False
    print(Solution().isIsomorphic("paper", "title"))  # True

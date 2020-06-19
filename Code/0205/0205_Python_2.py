class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        size_s = len(s)
        size_t = len(t)
        if size_s != size_t:
            return False

        hashmap_s = {}
        hashmap_t = {}
        for i in range(size_s):
            c_s = s[i]
            c_t = t[i]
            at_s = c_s in hashmap_s
            at_t = c_t in hashmap_t
            if at_s and at_t:
                if hashmap_s[c_s] != hashmap_t[c_t]:
                    return False
            elif (at_s and at_t) != (at_s or at_t):
                return False
            else:
                hashmap_s[c_s] = i
                hashmap_t[c_t] = i

        return True


if __name__ == "__main__":
    print(Solution().isIsomorphic("egg", "add"))  # True
    print(Solution().isIsomorphic("foo", "bar"))  # False
    print(Solution().isIsomorphic("paper", "title"))  # True

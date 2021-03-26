from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        hashmap = {}
        for c in A[0]:
            if c not in hashmap:
                hashmap[c] = 1
            else:
                hashmap[c] += 1

        for a in A[1:]:
            for k in hashmap:
                hashmap[k] = min(hashmap[k], a.count(k))

        ans = []
        for k, v in hashmap.items():
            while v > 0:
                ans.append(k)
                v -= 1

        return ans


if __name__ == "__main__":
    print(Solution().commonChars(["bella", "label", "roller"]))  # ["e","l","l"]
    print(Solution().commonChars(["cool", "lock", "cook"]))  # ["c","o"]

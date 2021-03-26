from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            ordered = "".join(sorted(s))
            if ordered not in hashmap:
                hashmap[ordered] = [s]
            else:
                hashmap[ordered].append(s)
        return [value for value in hashmap.values()]


if __name__ == "__main__":
    # [
    #   ["ate","eat","tea"],
    #   ["nat","tan"],
    #   ["bat"]
    # ]
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

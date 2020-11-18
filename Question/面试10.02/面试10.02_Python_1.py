from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sets = list({tuple(sorted(s)) for s in strs})
        dicts = {elem: i for i, elem in enumerate(sets)}

        ans = [[] for _ in range(len(sets))]
        for s in strs:
            ans[dicts[tuple(sorted(s))]].append(s)

        return ans


if __name__ == "__main__":
    # [
    #   ["ate","eat","tea"],
    #   ["nat","tan"],
    #   ["bat"]
    # ]
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

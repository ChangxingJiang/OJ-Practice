import collections
from typing import List


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        count = collections.defaultdict(list)
        for string in strings:
            key = []
            first = string[0]
            for ch in string:
                key.append((ord(ch) - ord(first) + 26) % 26)
            count[tuple(key)].append(string)
        return list(count.values())


if __name__ == "__main__":
    # [
    #   ["abc","bcd","xyz"],
    #   ["az","ba"],
    #   ["acef"],
    #   ["a","z"]
    # ]
    print(Solution().groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))

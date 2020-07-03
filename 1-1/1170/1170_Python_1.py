from typing import List


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        pass


if __name__ == "__main__":
    print(Solution().numSmallerByFrequency(queries=["cbd"], words=["zaaaz"]))  # [1]
    print(Solution().numSmallerByFrequency(queries=["bbb", "cc"], words=["a", "aa", "aaa", "aaaa"]))  # [1,2]

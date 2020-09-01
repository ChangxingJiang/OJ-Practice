import collections
from typing import List


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        # 整理子集列表
        count = collections.Counter()
        for b in B:
            tmp = collections.Counter(b)
            for key, value in tmp.items():
                count[key] = max(count[key], value)

        # 筛选单词
        ans = []
        for a in A:
            tmp = collections.Counter(a)
            for key, value in count.items():
                if count[key] > tmp[key]:
                    break
            else:
                ans.append(a)

        return ans


if __name__ == "__main__":
    print(Solution().wordSubsets(A=["amazon", "apple", "facebook", "google", "leetcode"], B=["e", "o"]))  # ["facebook","google","leetcode"]
    print(Solution().wordSubsets(A=["amazon", "apple", "facebook", "google", "leetcode"], B=["l", "e"]))  # ["apple","google","leetcode"]
    print(Solution().wordSubsets(A=["amazon", "apple", "facebook", "google", "leetcode"], B=["e", "oo"]))  # ["facebook","google"]
    print(Solution().wordSubsets(A=["amazon", "apple", "facebook", "google", "leetcode"], B=["lo", "eo"]))  # ["google","leetcode"]
    print(Solution().wordSubsets(A=["amazon", "apple", "facebook", "google", "leetcode"], B=["ec", "oc", "ceo"]))  # ["facebook","leetcode"]

import collections
from typing import List


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        # 整理子集列表
        count = {}
        for b in B:
            tmp = {}
            for ch in b:
                if ch not in tmp:
                    tmp[ch] = 1
                else:
                    tmp[ch] += 1
                if ch not in count:
                    count[ch] = 1
                else:
                    count[ch] = tmp[ch] if tmp[ch] > count[ch] else count[ch]

        # 生成模式
        s = []
        for ch in count:
            s.append(ch * count[ch])
        s = "".join(s)

        # 筛选单词
        ans = []
        for a in A:
            ans.append(a)
            for ch in s:
                if ch in a:
                    a = a.replace(ch, "", 1)
                else:
                    break
            else:
                continue
            ans.pop()
        return ans


if __name__ == "__main__":
    print(Solution().wordSubsets(A=["amazon", "apple", "facebook", "google", "leetcode"], B=["e", "o"]))  # ["facebook","google","leetcode"]
    print(Solution().wordSubsets(A=["amazon", "apple", "facebook", "google", "leetcode"], B=["l", "e"]))  # ["apple","google","leetcode"]
    print(Solution().wordSubsets(A=["amazon", "apple", "facebook", "google", "leetcode"], B=["e", "oo"]))  # ["facebook","google"]
    print(Solution().wordSubsets(A=["amazon", "apple", "facebook", "google", "leetcode"], B=["lo", "eo"]))  # ["google","leetcode"]
    print(Solution().wordSubsets(A=["amazon", "apple", "facebook", "google", "leetcode"], B=["ec", "oc", "ceo"]))  # ["facebook","leetcode"]

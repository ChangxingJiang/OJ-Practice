from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [""] * len(indices)
        for i1, i2 in enumerate(indices):
            res[i2] = s[i1]
        return "".join(res)


if __name__ == "__main__":
    print(Solution().restoreString(s="codeleet", indices=[4, 5, 6, 7, 0, 2, 1, 3]))  # "leetcode"
    print(Solution().restoreString(s="abc", indices=[0, 1, 2]))  # "abc"
    print(Solution().restoreString(s="aiohn", indices=[3, 1, 4, 2, 0]))  # "nihao"
    print(Solution().restoreString(s="aaiougrt", indices=[4, 0, 2, 6, 7, 3, 1, 5]))  # "arigatou"
    print(Solution().restoreString(s="art", indices=[1, 0, 2]))  # "rat"

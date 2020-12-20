from typing import List


class Solution:
    def findPermutation(self, s: str) -> List[int]:
        lst = [[0]]
        for ch in s:
            if ch == "I":
                lst.append([0])
            else:
                lst[-1].append(lst[-1][-1] - 1)

        ans = []
        max_val = 0
        for part in lst:
            min_val = part[-1] - 1
            for n in part:
                ans.append(max_val + n - min_val)
            max_val -= min_val

        return ans


if __name__ == "__main__":
    print(Solution().findPermutation("I"))  # [1,2]
    print(Solution().findPermutation("DI"))  # [2,1,3]
    print(Solution().findPermutation("DDIIDI"))  # [3,2,1,4,6,5,7]

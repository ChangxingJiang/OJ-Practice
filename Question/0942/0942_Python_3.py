from typing import List


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        ans = []
        a_min, a_max = 0, len(S)
        for s in S:
            if s == "I":
                ans.append(a_min)
                a_min += 1
            else:
                ans.append(a_max)
                a_max -= 1
        return ans + [a_min]


if __name__ == "__main__":
    print(Solution().diStringMatch("IDID"))  # [0,4,1,3,2]
    print(Solution().diStringMatch("III"))  # [0,1,2,3]
    print(Solution().diStringMatch("DDI"))  # [3,2,0,1]

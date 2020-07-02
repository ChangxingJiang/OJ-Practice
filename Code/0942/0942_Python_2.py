from typing import List


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        ans = [0]
        a_max = 0
        a_min = 0
        for s in S:
            if s == "I":
                a_max += 1
                ans.append(a_max)
            else:
                a_min -= 1
                ans.append(a_min)

        return [a - a_min for a in ans]


if __name__ == "__main__":
    print(Solution().diStringMatch("IDID"))  # [0,4,1,3,2]
    print(Solution().diStringMatch("III"))  # [0,1,2,3]
    print(Solution().diStringMatch("DDI"))  # [3,2,0,1]

from typing import List


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        ans = [0]
        for i in range(len(S)):
            if S[i] == "I":
                ans.append(i + 1)
            else:
                for j in range(len(ans)):
                    ans[j] += 1
                ans.append(0)
        return ans


if __name__ == "__main__":
    print(Solution().diStringMatch("IDID"))  # [0,4,1,3,2]
    print(Solution().diStringMatch("III"))  # [0,1,2,3]
    print(Solution().diStringMatch("DDI"))  # [3,2,0,1]

from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0]
        for i in range(1, num + 1):
            ans.append(ans[i & (i - 1)] + 1)
        return ans


if __name__ == "__main__":
    #  [0,1,1]
    print(Solution().countBits(2))

    # [0,1,1,2,1,2]
    print(Solution().countBits(5))

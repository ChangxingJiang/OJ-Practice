from typing import List


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        val = 0
        ans = []
        for a in A:
            val = (val << 1 ^ a) % 5
            ans.append(val== 0)
        return ans


if __name__ == "__main__":
    print(Solution().prefixesDivBy5([0, 1, 1]))  # [true,false,false]
    print(Solution().prefixesDivBy5([1, 1, 1]))  # [false,false,false]
    print(Solution().prefixesDivBy5([0, 1, 1, 1, 1, 1]))  # [true,false,false,false,true,false]
    print(Solution().prefixesDivBy5([1, 1, 1, 0, 1]))  # [false,false,false,false,false]

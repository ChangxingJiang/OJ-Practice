from typing import List


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        pass


if __name__ == "__main__":
    print(Solution().prefixesDivBy5([0, 1, 1]))  # [true,false,false]
    print(Solution().prefixesDivBy5([1, 1, 1]))  # [false,false,false]
    print(Solution().prefixesDivBy5([0, 1, 1, 1, 1, 1]))  # [true,false,false,false,true,false]
    print(Solution().prefixesDivBy5([1, 1, 1, 0, 1]))  # [false,false,false,false,false]

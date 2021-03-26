from typing import List


class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        ans = []
        for left, right, k in queries:
            differ = set()
            for i in range(left, right + 1):
                if s[i] in differ:
                    differ.remove(s[i])
                else:
                    differ.add(s[i])
            ans.append(len(differ) // 2 <= k)
        return ans


if __name__ == "__main__":
    # [true,false,false,true,true]
    print(Solution().canMakePaliQueries(s="abcda", queries=[[3, 3, 0], [1, 2, 0], [0, 3, 1], [0, 3, 2], [0, 4, 1]]))

    # [true,false,true,true,true,true,true,false,true,false,true,true,true]
    print(Solution().canMakePaliQueries(
        s="hunu",
        queries=[[1, 1, 1], [2, 3, 0], [3, 3, 1], [0, 3, 2], [1, 3, 3], [2, 3, 1], [3, 3, 1],
                 [0, 3, 0], [1, 1, 1], [2, 3, 0], [3, 3, 1], [0, 3, 1], [1, 1, 1]])
    )

from typing import List


class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        s = 0
        c = S[0]
        ans = []
        for i in range(1, len(S)):
            if S[i] != c:
                if i - s >= 3:
                    ans.append([s, i - 1])
                s = i
                c = S[i]
        else:
            if len(S) - s >= 3:
                ans.append([s, len(S) - 1])
        return ans


if __name__ == "__main__":
    print(Solution().largeGroupPositions("abbxxxxzzy"))  # [[3,6]]
    print(Solution().largeGroupPositions("abc"))  # []
    print(Solution().largeGroupPositions("abcdddeeeeaabbbcd"))  # [[3,5],[6,9],[12,14]]
    print(Solution().largeGroupPositions("aaa"))  # [[0,2]]

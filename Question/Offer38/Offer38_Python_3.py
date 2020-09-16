import collections
from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        ans = collections.deque([""])
        for ch in s:
            for _ in range(len(ans)):
                now = ans.popleft()
                for i in range((now + ch).index(ch) + 1):
                    ans.append(now[:i] + ch + now[i:])
        ans = list(set(ans))
        return ans


if __name__ == "__main__":
    # ["abc","acb","bac","bca","cab","cba"]
    print(Solution().permutation("abc"))

    # ["aba","aab","baa"]
    print(Solution().permutation("aab"))

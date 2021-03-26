from typing import List


class Solution:
    _MOD = 10 ** 9 + 7

    def threeSumMulti(self, A: List[int], target: int) -> int:
        A.sort()
        ans = 0
        for i in range(len(A)):
            j, k = i + 1, len(A) - 1
            while j <= k:
                if A[i] + A[j] + A[k] < target:
                    j += 1
                elif A[i] + A[j] + A[k] > target:
                    k -= 1
                elif A[j] != A[k]:
                    left = right = 1
                    while j + 1 < k and A[j] == A[j + 1]:
                        left += 1
                        j += 1
                    while k - 1 > j and A[k] == A[k - 1]:
                        right += 1
                        k -= 1
                    ans += left * right
                    ans %= self._MOD
                    j += 1
                    k -= 1
                else:
                    ans += (k - j + 1) * (k - j) // 2
                    ans %= self._MOD
                    break

        return ans


if __name__ == "__main__":
    print(Solution().threeSumMulti(A=[1, 1, 2, 2, 3, 3, 4, 4, 5, 5], target=8))  # 20
    print(Solution().threeSumMulti(A=[1, 1, 2, 2, 2, 2], target=5))  # 12

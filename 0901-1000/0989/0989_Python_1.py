from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        carry = 0
        ans = []
        while len(A) > 0 or K > 0 or carry > 0:
            if len(A) > 0:
                a = A.pop(-1)
            else:
                a = 0

            if K > 0:
                b = K % 10
                K //= 10
            else:
                b = 0

            t = a + b + carry
            ans.append(t % 10)
            carry = t // 10
        return ans[::-1]


if __name__ == "__main__":
    print(Solution().addToArrayForm(A=[1, 2, 0, 0], K=34))  # [1,2,3,4]
    print(Solution().addToArrayForm(A=[2, 7, 4], K=181))  # [4,5,5]
    print(Solution().addToArrayForm(A=[2, 1, 5], K=806))  # [1,0,2,1]
    print(Solution().addToArrayForm(A=[9, 9, 9, 9, 9, 9, 9, 9, 9, 9], K=1))  # [1,0,0,0,0,0,0,0,0,0,0]

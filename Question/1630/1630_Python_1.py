from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        def is_equal(ll):
            ll.sort()

            if len(ll) <= 2:
                return True

            d = ll[1] - ll[0]
            for j in range(2, len(ll)):
                if ll[j] - ll[j - 1] != d:
                    return False

            return True

        m = len(l)

        ans = []

        for i in range(m):
            left = l[i]
            right = r[i]

            lst = nums[left:right + 1]
            ans.append(is_equal(lst))

        return ans


if __name__ == "__main__":
    # [true,false,true]
    print(Solution().checkArithmeticSubarrays(nums=[4, 6, 5, 9, 3, 7], l=[0, 0, 2], r=[2, 3, 5]))

    # [false,true,false,false,true,true]
    print(Solution().checkArithmeticSubarrays(nums=[-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10],
                                              l=[0, 1, 6, 4, 8, 7], r=[4, 4, 9, 7, 9, 10]))

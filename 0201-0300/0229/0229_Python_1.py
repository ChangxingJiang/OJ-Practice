from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # 摩尔投票
        n1_val, n1_num = 0, 0
        n2_val, n2_num = 0, 0
        for num in nums:
            if num == n1_val:
                n1_num += 1
            elif num == n2_val:
                n2_num += 1
            else:  # num != n1_val and num != n2_val
                if n1_num == 0:
                    n1_val, n1_num = num, 1
                    continue
                elif n2_num == 0:
                    n2_val, n2_num = num, 1
                    continue
                else:
                    n1_num -= 1
                    n2_num -= 1

        # 计票确认
        n1_num, n2_num = 0, 0
        for num in nums:
            if num == n1_val:
                n1_num += 1
            elif num == n2_val:
                n2_num += 1

        target = len(nums) / 3

        ans = []
        if n1_num > target:
            ans.append(n1_val)
        if n2_num > target:
            ans.append(n2_val)
        return ans


if __name__ == "__main__":
    # [3]
    print(Solution().majorityElement([3, 2, 3]))

    # [1]
    print(Solution().majorityElement([1]))

    # [1,2]
    print(Solution().majorityElement([1, 1, 1, 3, 3, 2, 2, 2]))

from typing import List


class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        # 生成s中每一个位置的前缀字母情况
        nums = [0] * 26
        lst = [nums.copy()]
        for ch in s:
            nums[ord(ch) - 97] += 1
            lst.append(nums.copy())

        # 遍历计算每一个query是否为回文串
        ans = []
        for left, right, k in queries:
            differ = 0
            left_nums = lst[left]
            right_nums = lst[right + 1]
            for i in range(26):
                if (right_nums[i] - left_nums[i]) % 2 == 1:
                    differ += 1
            # print(left, right, k, differ, left_nums, right_nums)
            ans.append(differ // 2 <= k)

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

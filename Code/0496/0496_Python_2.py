from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 生成下一个更大元素对应哈希表
        hashmap = {}
        stack = []
        for num in nums2:
            while stack:
                if stack[-1] < num:
                    hashmap[stack.pop(-1)] = num
                else:
                    break
            stack.append(num)
        for num in stack:
            hashmap[num] = -1

        # 返回结果
        return [hashmap[num] for num in nums1]


if __name__ == "__main__":
    print(Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))  # [-1,3,-1]
    print(Solution().nextGreaterElement([2, 4], [1, 2, 3, 4]))  # [3,-1]

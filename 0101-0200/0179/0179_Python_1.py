from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 自定义排序：在数字后补齐到10位，补的内容为数字前面的开头
        ans = "".join(sorted([str(num) for num in nums], key=lambda x: (10 * x)[:10], reverse=True)).lstrip("0")
        return ans if ans else "0"


if __name__ == "__main__":
    print(Solution().largestNumber(nums=[10, 2]))  # "210"
    print(Solution().largestNumber(nums=[3, 30, 34, 5, 9]))  # "9534330"
    print(Solution().largestNumber(nums=[1]))  # "1"
    print(Solution().largestNumber(nums=[10]))  # "10"
    print(Solution().largestNumber(nums=[0, 0]))  # "0"

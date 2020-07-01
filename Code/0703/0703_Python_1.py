from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.nums.sort()

    def add(self, val: int) -> int:
        left = 0
        right = len(self.nums)
        idx = (left + right) // 2
        while left < right:
            if val < self.nums[idx]:
                right = idx
            elif val > self.nums[idx]:
                left = idx + 1
            else:
                break
            idx = (left + right) // 2
        self.nums.insert(idx, val)
        return self.nums[-self.k]


if __name__ == "__main__":
    k = 3
    arr = [4, 5, 8, 2]
    kthLargest = KthLargest(3, arr)
    print(kthLargest.add(3))  # 4
    print(kthLargest.add(5))  # 5
    print(kthLargest.add(10))  # 5
    print(kthLargest.add(9))  # 8
    print(kthLargest.add(4))  # 8

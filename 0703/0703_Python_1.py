from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        pass

    def add(self, val: int) -> int:
        pass


if __name__ == "__main__":
    k = 3
    arr = [4, 5, 8, 2]
    kthLargest = KthLargest(3, arr)
    kthLargest.add(3)  # 4
    kthLargest.add(5)  # 5
    kthLargest.add(10)  # 5
    kthLargest.add(9)  # 8
    kthLargest.add(4)  # 8

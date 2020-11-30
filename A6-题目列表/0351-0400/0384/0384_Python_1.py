from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        pass

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """


if __name__ == "__main__":
    obj = Solution([1, 2, 3])
    print(obj.shuffle())  # [3,1,2]
    print(obj.reset())  # [1,2,3]
    print(obj.shuffle())  # [1,3,2]

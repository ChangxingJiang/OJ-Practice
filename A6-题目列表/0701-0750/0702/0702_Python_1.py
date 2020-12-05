# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """


if __name__ == "__main__":
    print(Solution().search(reader=[-1, 0, 3, 5, 9, 12], target=9))  # 4
    print(Solution().search(reader=[-1, 0, 3, 5, 9, 12], target=2))  # -1

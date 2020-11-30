# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """

    def next(self):
        """
        :rtype: int
        """

    def hasNext(self):
        """
        :rtype: bool
        """


if __name__ == "__main__":
    obj = PeekingIterator([1, 2, 3])
    print(obj.next())  # 1
    print(obj.peek())  # 2
    print(obj.next())  # 2
    print(obj.next())  # 3
    print(obj.hasNext())  # False

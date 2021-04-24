class AVL:
    """自平衡二叉树"""

    class _Node:
        __slots__ = ("_element", "_parent", "_left", "_right", "_height")

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right
            self._height = 0

        @property
        def element(self):
            return self._element

        @property
        def left(self):
            return self._left

        @property
        def right(self):
            return self._right

        @property
        def parent(self):
            return self._parent

        @property
        def height(self):
            return self._height

        def left_height(self):
            return self._left.height if self._left is not None else 0

        def right_right(self):
            return self._right.height if self._right is not None else 0


class MKAverage:

    def __init__(self, m: int, k: int):
        pass

    def addElement(self, num: int) -> None:
        pass

    def calculateMKAverage(self) -> int:
        pass


if __name__ == "__main__":
    obj = MKAverage(3, 1)
    obj.addElement(3)
    obj.addElement(1)
    print(obj.calculateMKAverage())  # -1
    obj.addElement(10)
    print(obj.calculateMKAverage())  # 3
    obj.addElement(5)
    obj.addElement(5)
    obj.addElement(5)
    print(obj.calculateMKAverage())  # 5

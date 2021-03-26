# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
class Sea(object):
    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
        pass


class Point(object):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        pass


if __name__ == "__main__":
    pass

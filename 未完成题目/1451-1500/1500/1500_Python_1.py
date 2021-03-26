from typing import List


class FileSharing:

    def __init__(self, m: int):
        pass

    def join(self, ownedChunks: List[int]) -> int:
        pass

    def leave(self, userID: int) -> None:
        pass

    def request(self, userID: int, chunkID: int) -> List[int]:
        pass


if __name__ == "__main__":
    obj = FileSharing(4)
    print(obj.join([1, 2]))  # 1
    print(obj.join([2, 3]))  # 2
    print(obj.join([4]))  # 3
    print(obj.request(1, 3))  # [2]
    print(obj.request(2, 2))  # [1,2]
    obj.leave(1)
    print(obj.request(2, 1))  # []
    obj.leave(2)
    print(obj.join([]))  # 1

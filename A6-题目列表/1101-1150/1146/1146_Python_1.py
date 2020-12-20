class SnapshotArray:

    def __init__(self, length: int):
        pass

    def set(self, index: int, val: int) -> None:
        pass

    def snap(self) -> int:
        pass

    def get(self, index: int, snap_id: int) -> int:
        pass


if __name__ == "__main__":
    obj = SnapshotArray(3)
    obj.set(0, 5)
    print(obj.snap())  # 0
    obj.set(0, 6)
    print(obj.get(0, 0))  # 5

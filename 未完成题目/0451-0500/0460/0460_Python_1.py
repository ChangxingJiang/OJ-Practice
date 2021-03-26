class LFUCache:

    def __init__(self, capacity: int):
        pass

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass


if __name__ == "__main__":
    obj = LFUCache(2)
    obj.put(1, 1)
    obj.put(2, 2)
    print(obj.get(1))  # 1
    obj.put(3, 3)
    print(obj.get(2))  # -1
    print(obj.get(3))  # 3
    obj.put(4, 4)
    print(obj.get(1))  # -1
    print(obj.get(3))  # 3
    print(obj.get(4))  # 4

from typing import List


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        pass

    def q(self, t: int) -> int:
        pass


if __name__ == "__main__":
    obj = TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30])
    print(obj.q(3))  # 0
    print(obj.q(12))  # 1
    print(obj.q(25))  # 1
    print(obj.q(15))  # 0
    print(obj.q(24))  # 0
    print(obj.q(8))  # 1

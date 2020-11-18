from typing import List
import collections

class AnimalShelf:

    def __init__(self):
        self.idx = 0
        self.cats = collections.deque([])
        self.dogs = collections.deque([])

    def enqueue(self, animal: List[int]) -> None:
        if animal[1] == 0:
            self.cats.append((self.idx, animal))
        else:
            self.dogs.append((self.idx, animal))
        self.idx += 1

    def dequeueAny(self) -> List[int]:
        if not self.cats and not self.dogs:
            return [-1, -1]
        elif not self.cats:
            return self.dogs.popleft()[1]
        elif not self.dogs:
            return self.cats.popleft()[1]
        else:
            if self.dogs[0][0] < self.cats[0][0]:
                return self.dogs.popleft()[1]
            else:
                return self.cats.popleft()[1]

    def dequeueDog(self) -> List[int]:
        if not self.dogs:
            return [-1,-1]
        else:
            return self.dogs.popleft()[1]

    def dequeueCat(self) -> List[int]:
        if not self.cats:
            return [-1, -1]
        else:
            return self.cats.popleft()[1]


if __name__ == "__main__":
    animals = AnimalShelf()
    animals.enqueue([0, 0])
    animals.enqueue([1, 0])
    print(animals.dequeueCat())  # [0,0]
    print(animals.dequeueDog())  # [-1,-1]
    print(animals.dequeueAny())  # [1,0]

    animals = AnimalShelf()
    animals.enqueue([0, 0])
    animals.enqueue([1, 0])
    animals.enqueue([2, 1])
    print(animals.dequeueDog())  # [2,1]
    print(animals.dequeueCat())  # [0,0]
    print(animals.dequeueAny())  # [1,0]

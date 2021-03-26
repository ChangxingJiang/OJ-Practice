from typing import List


class Solution:
    def orientation(self, p, q, r):
        return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        if len(points) <= 1:
            return points

        points.sort()

        stack = []
        for point in points:
            while len(stack) >= 2 and self.orientation(stack[-2], stack[-1], point) > 0:
                stack.pop()
            stack.append(point)

        stack.pop()
        for point in reversed(points):
            while len(stack) >= 2 and self.orientation(stack[-2], stack[-1], point) > 0:
                stack.pop()
            stack.append(point)
        stack.pop()

        return list([point[0], point[1]] for point in set((point[0], point[1]) for point in stack))


if __name__ == "__main__":
    # [[1,1],[2,0],[4,2],[3,3],[2,4]]
    print(Solution().outerTrees([[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]))

    # [[1,2],[2,2],[4,2]]
    print(Solution().outerTrees([[1, 2], [2, 2], [4, 2]]))

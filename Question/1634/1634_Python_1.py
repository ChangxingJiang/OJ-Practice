class PolyNode:
    def __init__(self, x=0, y=0, next=None):
        self.coefficient = x
        self.power = y
        self.next = next


class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        ans = node = PolyNode(0, 0)
        while poly1 and poly2:
            if poly1.power > poly2.power:
                node.next = PolyNode(poly1.coefficient, poly1.power)
                node = node.next
                poly1 = poly1.next
            elif poly1.power < poly2.power:
                node.next = PolyNode(poly2.coefficient, poly2.power)
                node = node.next
                poly2 = poly2.next
            else:
                coefficient = poly1.coefficient + poly2.coefficient
                if coefficient != 0:
                    node.next = PolyNode(coefficient, poly1.power)
                    node = node.next
                poly1 = poly1.next
                poly2 = poly2.next
        if poly1:
            node.next = poly1
        if poly2:
            node.next = poly2
        return ans.next


if __name__ == "__main__":
    p1 = PolyNode(1, 1)
    p2 = PolyNode(1, 0)
    print(Solution().addPoly(p1, p2))

    p13 = PolyNode(3, 0)
    p12 = PolyNode(4, 1, p13)
    p11 = PolyNode(2, 2, p12)
    p23 = PolyNode(-1, 0)
    p22 = PolyNode(-4, 1, p23)
    p21 = PolyNode(3, 2, p22)
    print(Solution().addPoly(p1, p2))

    p1 = PolyNode(1, 2)
    p2 = PolyNode(-1, 2)
    print(Solution().addPoly(p1, p2))

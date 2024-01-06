import pytest
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def solve(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p = 0
        a = []
        while l1 is not None or l2 is not None:
            s = p
            if l1 is not None:
                s += l1.val
                l1 = l1.next
            if l2 is not None:
                s += l2.val
                l2 = l2.next
            a.append(s % 10)
            p = s // 10
        if p > 0:
            a.append(p)
        ans = [ListNode(val=a[-1], next=None)]
        for i in range(len(a) - 2, -1, -1):
            ans.append(ListNode(val=a[i], next=ans[-1]))
        return ans[-1]


def create_list_node_from_list(lst: list) -> Optional[ListNode]:
    ans = [ListNode(val=lst[-1], next=None)]
    for i in range(len(lst) - 2, -1, -1):
        ans.append(ListNode(val=lst[i], next=ans[-1]))
    return ans[-1]


def create_list_from_list_node(lst: Optional[ListNode]) -> list:
    ans = []
    while lst is not None:
        ans.append(lst.val)
        lst = lst.next
    return ans


@pytest.mark.parametrize("first_list, second_list, expected_list", [
    ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
    ([0], [0], [0]),
    ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1])
])
def test_problem(first_list, second_list, expected_list):
    solution = Solution()
    ln_1 = create_list_node_from_list(first_list)
    ln_2 = create_list_node_from_list(second_list)
    ans = create_list_from_list_node(solution.solve(ln_1, ln_2))
    assert ans == expected_list

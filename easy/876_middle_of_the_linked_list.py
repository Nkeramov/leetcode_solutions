from typing import Optional
import pytest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def solve(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        while head is not None:
            a.append(head.val)
            head = head.next
        a = a[len(a) // 2:]
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


@pytest.mark.parametrize("input_list, expected_list", [
    ([1, 2, 3, 4, 5], [3, 4, 5]),
    ([1, 2, 3, 4, 5, 6], [4, 5, 6])
])
def test_problem(input_list, expected_list):
    solution = Solution()
    ln = create_list_node_from_list(input_list)
    ans = create_list_from_list_node(solution.solve(ln))
    assert ans == expected_list

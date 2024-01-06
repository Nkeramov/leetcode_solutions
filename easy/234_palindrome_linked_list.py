import pytest
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def solve(self, head: Optional[ListNode]) -> bool:
        a = []
        while head is not None:
            a.append(head.val)
            head = head.next
        for i in range(len(a) // 2):
            if a[i] != a[len(a) - 1 - i]:
                return False
        return True

    def test(self):
        test_cases = [

        ]
        for i, test_case in enumerate(test_cases):
            head = self.create_listnode_from_list(test_case[0])
            ans = self.solve(head)
            correct_ans = test_case[-1]
            assert ans == correct_ans, f"Case {i} error, your answer is {ans}, but correct answer is {correct_ans}"
        print("All tests are successfully")



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


@pytest.mark.parametrize("input_list, expected_value", [
    ([1, 2, 2, 1], True),
    ([1, 2], False),
    ([1], True)
])
def test_problem(input_list, expected_value):
    solution = Solution()
    head = create_list_node_from_list(input_list)
    ans = solution.solve(head)
    assert ans == expected_value

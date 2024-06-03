import pytest
from typing import List
from collections import deque


class Solution:
    def solve(self, nums: List[int], k: int) -> List[int]:
        ans = []
        wnd = deque()
        for i, num in enumerate(nums):
            while wnd and wnd[0] < i - k + 1:
                wnd.popleft()
            while wnd and nums[wnd[-1]] < num:
                wnd.pop()
            wnd.append(i)
            if i >= k - 1:
                ans.append(nums[wnd[0]])
        return ans


@pytest.mark.parametrize("nums, k, expected_value", [
    ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
    ([1], 1, [1])
])
def test_problem(ransom_note, magazine, expected_value):
    solution = Solution()
    assert solution.solve(ransom_note, magazine) == expected_value

import pytest
from typing import List


class Solution:
    def solve(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 1],cost[i - 2])
        return min(cost[-1], cost[-2])


@pytest.mark.parametrize("cost, expected_value", [
    ([10,15,20], 15),
    ([1,100,1,1,1,100,1,1,100,1], 6)
])
def test_problem(cost, expected_value):
    solution = Solution()
    ans = solution.solve(cost)
    assert ans == expected_value

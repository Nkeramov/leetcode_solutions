import pytest
from typing import List


class Solution:
    def solve(self, bills: List[int]) -> bool:
        count5, count10 = 0, 0
        for b in bills:
            if b == 5:
                count5 += 1
            elif b == 10:
                if count5 == 0:
                    return False
                count5 -= 1
                count10 += 1
            else:
                if count10 > 0 and count5 > 0:
                    count10 -= 1
                    count5 -= 1
                elif count5 >= 3:
                    count5 -= 3
                else:
                    return False
        return True


@pytest.mark.parametrize("bills, expected_value", [
    ([5, 5, 5, 10, 20], True),
    ([5, 5, 10, 5, 20], True),
    ([5, 5, 10, 20, 5], True),
    ([5, 5, 10, 20, 10], False),
    ([5, 5, 10, 10, 20], False)
])
def test_problem(bills, expected_value):
    solution = Solution()
    ans = solution.solve(bills)
    assert ans == expected_value

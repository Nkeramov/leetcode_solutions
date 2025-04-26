import pytest
from typing import List


class Solution:
    def solve(self, x: int, y: int, bound: int) -> List[int]:
        ans = set()
        a = 1
        while a <= bound:
            b = 1
            while a + b <= bound:
                ans.add(a + b)
                b *= y
                if y == 1:
                    break
            if x == 1:
                break
            a *= x
        return list(ans)


@pytest.mark.parametrize("x, y, bound, expected_value", [
    (2, 3, 10, [2, 3, 4, 5, 7, 9, 10]),
    (3, 5, 15, [2, 4, 6, 8, 10, 14])
])
def test_problem(x, y, bound, expected_value):
    solution = Solution()
    ans = solution.solve(x, y, bound)
    assert ans == expected_value



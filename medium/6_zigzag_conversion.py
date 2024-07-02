import pytest


class Solution:
    def solve(self, s: str, num_rows: int) -> str:
        if num_rows == 1 or len(s) < num_rows:
            return s
        st = [''] * num_rows
        step, row = -1, 0
        for i, c in enumerate(s):
            st[row] += c
            if row == 0 or row == num_rows - 1:
                step = -step
            row += step
        return ''.join(st)


@pytest.mark.parametrize("s, num_rows, expected_value", [
    ('PAYPALISHIRING', 3, 'PAHNAPLSIIGYIR'),
    ('PAYPALISHIRING', 4, 'PINALSIGYAHRPI'),
    ('QWE', 2, 'QEW'),
    ('A', 1, 'A')
])
def test_problem(s, num_rows, expected_value):
    solution = Solution()
    ans = solution.solve(s, num_rows)
    assert ans == expected_value

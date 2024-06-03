import pytest
from operator import itemgetter
from typing import List


class Solution:
    def solve(self, mat: List[List[int]], k: int) -> List[int]:
        d = []
        for i in range(len(mat)):
            d.append({'i': i, 'cnt': mat[i].count(1)})
        sd = sorted(d, key=itemgetter('cnt'))
        return [x['i'] for x in sd[:k]]


@pytest.mark.parametrize("mat, k, expected_value", [
    ([[1, 1, 0, 0, 0],
      [1, 1, 1, 1, 0],
      [1, 0, 0, 0, 0],
      [1, 1, 0, 0, 0],
      [1, 1, 1, 1, 1]], 3, [2, 0, 3]),
    ([[1, 0, 0, 0],
      [1, 1, 1, 1],
      [1, 0, 0, 0],
      [1, 0, 0, 0]], 2, [0, 2])
])
def test_problem(mat, k, expected_value):
    solution = Solution()
    ans = solution.solve(mat, k)
    assert ans == expected_value

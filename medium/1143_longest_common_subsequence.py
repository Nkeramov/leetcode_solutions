import pytest


class Solution:
    def solve(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        least_common_suffixes = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    least_common_suffixes[i][j] = least_common_suffixes[i - 1][j - 1] + 1
                else:
                    least_common_suffixes[i][j] = max(least_common_suffixes[i - 1][j], least_common_suffixes[i][j - 1])
        return least_common_suffixes[m][n]
        # lcs = []
        # i, j = m, n
        # while i > 0 and j > 0:
        #     if text1[i - 1] == text2[j - 1]:
        #         lcs.append(text1[i - 1])
        #         i -= 1
        #         j -= 1
        #     elif least_common_suffixes[i - 1][j] > least_common_suffixes[i][j - 1]:
        #         i -= 1
        #     else:
        #         j -= 1
        # lcs.reverse()
        # return ''.join(lcs)


@pytest.mark.parametrize("first_input_value, second_input_value, expected_value", [
    ("abcde", "ace", 3), ("abc", "abc", 3), ("abc", "def", 0)
])
def test_problem(first_input_value, second_input_value, expected_value):
    solution = Solution()
    ans = solution.solve(first_input_value, second_input_value)
    assert ans == expected_value

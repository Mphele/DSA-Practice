import unittest


# Exercise 07: Container With Most Water
#
# Source: https://leetcode.com/problems/container-with-most-water/
# Original difficulty: Medium
#
# Task:
# You are given a list in which each value is the height of a vertical line.
# The line's index is its horizontal position. Choose two lines that, together
# with the horizontal axis, enclose the greatest possible area. Return that
# area. The lines must remain vertical.
#
# Examples:
#   heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
#   return 49
#
#   heights = [1, 1]
#   return 1
#
# Constraints:
# - 2 <= len(heights) <= 100_000
# - 0 <= heights[i] <= 10_000
def max_container_area(heights: list) -> int:
    left = 0
    right = len(heights) - 1
    max_area = 0

    while left < right:
        width = right - left
        usable_height = min(heights[left], heights[right])
        current_area = width * usable_height

        max_area = max(max_area, current_area)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_area

class MaxContainerAreaTests(unittest.TestCase):
    def test_standard_case(self):
        self.assertEqual(max_container_area([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

    def test_two_lines(self):
        self.assertEqual(max_container_area([1, 1]), 1)

    def test_zero_heights(self):
        self.assertEqual(max_container_area([0, 0]), 0)

    def test_equal_heights(self):
        self.assertEqual(max_container_area([5, 5, 5, 5]), 15)

    def test_best_pair_is_inside_the_boundaries(self):
        self.assertEqual(max_container_area([1, 100, 100, 1]), 100)

    def test_maximum_allowed_heights(self):
        self.assertEqual(max_container_area([10_000, 0, 0, 10_000]), 30_000)

    def test_decreasing_heights(self):
        self.assertEqual(max_container_area([5, 4, 3, 2, 1]), 6)


if __name__ == "__main__":
    unittest.main(verbosity=2)

import unittest


# Exercise 09: Search Insert Position
#
# Source: https://leetcode.com/problems/search-insert-position/
# Original difficulty: Easy
#
# Task:
# Given an ascending list of distinct integers and a target, return the
# target's index when it is present. If it is absent, return the index where
# it could be inserted while keeping the list sorted.
#
# Examples:
#   numbers = [1, 3, 5, 6], target = 5
#   return 2
#
#   numbers = [1, 3, 5, 6], target = 2
#   return 1
#
# Constraints:
# - 1 <= len(numbers) <= 10_000
# - -10_000 <= numbers[i], target <= 10_000
# - numbers contains distinct values in ascending order
# - The required runtime is O(log n)
def find_insert_position(numbers: list[int], target: int) -> int:

    last_smaller_index =-1

    for index,num in enumerate(numbers):
        if num ==target:
            return index

        if num<target:
            last_smaller_index=index

        if num>target:
            return last_smaller_index +1

    return last_smaller_index+1




class SearchInsertPositionTests(unittest.TestCase):
    def test_target_is_present(self):
        self.assertEqual(find_insert_position([1, 3, 5, 6], 5), 2)

    def test_insert_between_values(self):
        self.assertEqual(find_insert_position([1, 3, 5, 6], 2), 1)

    def test_insert_after_last_value(self):
        self.assertEqual(find_insert_position([1, 3, 5, 6], 7), 4)

    def test_insert_before_first_value(self):
        self.assertEqual(find_insert_position([1, 3, 5, 6], 0), 0)

    def test_single_value_present(self):
        self.assertEqual(find_insert_position([4], 4), 0)

    def test_single_value_insert_after(self):
        self.assertEqual(find_insert_position([4], 9), 1)

    def test_negative_values(self):
        self.assertEqual(find_insert_position([-8, -4, 0, 7], -3), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)

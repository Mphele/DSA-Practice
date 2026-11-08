import unittest
import math


# Minimum Size Subarray Sum
#
# Source: https://leetcode.com/problems/minimum-size-subarray-sum/
# Original difficulty: Medium
#
# Given a positive integer `target` and a list of positive integers `nums`,
# return the smallest length of a contiguous subarray whose sum is greater
# than or equal to `target`.
#
# A subarray must contain consecutive values from the original list. You may
# not skip values or reorder the input.
#
# Return 0 when no qualifying subarray exists.
#
# Requirements:
# - Solve the problem in O(n) time.
#
# Examples:
#   target = 7
#   nums = [2, 3, 1, 2, 4, 3]
#   return 2
#   Explanation: [4, 3] has a sum of 7.
#
#   target = 4
#   nums = [1, 4, 4]
#   return 1
#
#   target = 11
#   nums = [1, 1, 1, 1, 1, 1, 1, 1]
#   return 0
#
# Constraints:
# - 1 <= target <= 1_000_000_000
# - 1 <= len(nums) <= 100_000
# - 1 <= nums[i] <= 10_000
def minimum_subarray_length(target, nums):
    found = False
    current = 0
    min_num = len(nums)
    sum=0
    for num in nums:
        if num==target:
            return 1

        current+=1
        sum+=num
        if sum >= target:
                found=True
                if current<min_num:
                    min_num = current
                current =0
                sum = 0 

        



    return min_num if found else 0
                



class MinimumSubarrayLengthTests(unittest.TestCase):
    def test_shortest_is_near_end(self):
        self.assertEqual(minimum_subarray_length(7, [2, 3, 1, 2, 4, 3]), 2)

    def test_single_value_reaches_target(self):
        self.assertEqual(minimum_subarray_length(4, [1, 4, 4]), 1)

    def test_no_qualifying_subarray(self):
        self.assertEqual(
            minimum_subarray_length(11, [1, 1, 1, 1, 1, 1, 1, 1]),
            0,
        )

    def test_entire_list_is_required(self):
        self.assertEqual(minimum_subarray_length(15, [1, 2, 3, 4, 5]), 5)

    def test_one_element_input(self):
        self.assertEqual(minimum_subarray_length(5, [5]), 1)

    def test_exact_sum_using_entire_list(self):
        self.assertEqual(minimum_subarray_length(6, [1, 2, 3]), 3)

    def test_shortest_sum_exceeds_target(self):
        self.assertEqual(minimum_subarray_length(11, [1, 2, 3, 4, 5]), 3)

    def test_first_element_reaches_target(self):
        self.assertEqual(minimum_subarray_length(7, [7, 1, 1]), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)

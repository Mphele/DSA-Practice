import unittest
import math

# Product of Array Except Self
#
# Given an integer array `nums`, return an array `answer` where `answer[i]`
# equals the product of every element in `nums` except `nums[i]`.
#
# Requirements:
# - Solve the problem in O(n) time.
# - Do not use division.
#
# Examples:
#   nums = [1, 2, 3, 4]
#   return [24, 12, 8, 6]
#
#   nums = [-1, 1, 0, -3, 3]
#   return [0, 0, 9, 0, 0]
#
# Constraints:
# - 2 <= len(nums) <= 100000
# - -30 <= nums[i] <= 30
# - Every prefix or suffix product fits within a normal integer.
def product_except_self(nums):
    answer = []

    for i in range(len(nums)):
        i_change=0
        product = 1
        while i>0:
            product*=nums[i-1]
            i-=1
            i_change+=1

        i+=i_change
        while i<len(nums)-1:
            product*=nums[i+1]
            i+=1

        answer.append(product)

        
    return answer

class ProductExceptSelfTests(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(product_except_self([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_one_zero(self):
        self.assertEqual(
            product_except_self([-1, 1, 0, -3, 3]),
            [0, 0, 9, 0, 0],
        )

    def test_two_zeros(self):
        self.assertEqual(product_except_self([0, 4, 0]), [0, 0, 0])

    def test_negative_numbers(self):
        self.assertEqual(product_except_self([-1, -2, -3]), [6, 3, 2])

    def test_two_values(self):
        self.assertEqual(product_except_self([2, 5]), [5, 2])

    def test_repeated_ones(self):
        self.assertEqual(product_except_self([1, 1, 1, 1]), [1, 1, 1, 1])


if __name__ == "__main__":
    unittest.main(verbosity=2)

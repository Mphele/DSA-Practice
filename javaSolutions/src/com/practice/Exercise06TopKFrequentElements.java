package com.practice;

import java.util.Arrays;
import java.util.*;

public class Exercise06TopKFrequentElements {

    /*
     * Exercise 06: Top K Frequent Elements
     *
     * Source: https://leetcode.com/problems/top-k-frequent-elements/
     * Original difficulty: Medium
     *
     * Task:
     * Given an integer array and an integer k, return the k values that occur
     * most often. The returned values may be in any order. The input is
     * guaranteed to have one unambiguous set of k answers.
     *
     * Examples:
     *   nums = [1, 1, 1, 2, 2, 3], k = 2
     *   return [1, 2]
     *
     *   nums = [1], k = 1
     *   return [1]
     *
     * Constraints:
     * - 1 <= nums.length <= 100_000
     * - -10_000 <= nums[i] <= 10_000
     * - 1 <= k <= the number of distinct values in nums
     * - The answer is guaranteed to be unique.
     * - The runtime must be better than O(n log n).
     */
    public static int[] topKFrequent(int[] nums, int k) {

        Map<Integer, Integer> frequency = new HashMap<>();

        for(int num:nums){
            int currentCount = frequency.getOrDefault(num,0);
            frequency.put(num, currentCount+1);
        }

        List<Integer> values = new ArrayList<>(frequency.values());

        values.sort(Comparator.reverseOrder());

        List<Integer> kValues = new ArrayList<>();

        for(int i=0; i<k; i++){
            kValues.add(values.get(i));
        }
        int[] mostFrequent = new int[k];
        int index =0;
        for(int num: frequency.keySet()){

            if(kValues.contains(frequency.get(num))){
                mostFrequent[index] = num;
                index++;
            }

        }

        return mostFrequent;


    }

    private static String normalized(int[] values) {
        if (values == null) {
            return "null";
        }

        int[] copy = Arrays.copyOf(values, values.length);
        Arrays.sort(copy);
        return Arrays.toString(copy);
    }

    private static void runCase(String name, int[] nums, int k, int[] expected) {
        int[] actual = topKFrequent(nums, k);
        String normalizedExpected = normalized(expected);
        String normalizedActual = normalized(actual);
        boolean passed = normalizedExpected.equals(normalizedActual);

        System.out.println((passed ? "PASS" : "FAIL") + " - " + name);
        System.out.println("  expected: " + normalizedExpected);
        System.out.println("  actual:   " + normalizedActual);
    }

    public static void main(String[] args) {
        runCase(
                "standard frequencies",
                new int[] {1, 1, 1, 2, 2, 3},
                2,
                new int[] {1, 2});

        runCase(
                "single value",
                new int[] {7},
                1,
                new int[] {7});

        runCase(
                "negative values",
                new int[] {-1, -1, -2, -2, -2, 3},
                2,
                new int[] {-2, -1});

        runCase(
                "all distinct values requested",
                new int[] {4, 4, 5, 6, 6, 6},
                3,
                new int[] {4, 5, 6});

        runCase(
                "one dominant value",
                new int[] {10, 10, 10, -1, -1, 2, 3},
                1,
                new int[] {10});

        runCase(
                "constraint boundary values",
                new int[] {-10000, -10000, 10000, 4, 4, 4},
                2,
                new int[] {-10000, 4});
    }
}

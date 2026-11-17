package com.practice;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Exercise10BestTimeToBuyAndSellStock {

    /*
     * Exercise 10: Best Time to Buy and Sell Stock
     *
     * Source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
     * Original difficulty: Easy
     *
     * Task:
     * Each element in prices is the price of one stock on that day. Choose
     * one day to buy and a later day to sell so that the profit is as large
     * as possible. Return that profit. Return 0 when no profitable trade is
     * possible.
     *
     * Examples:
     *   prices = [7, 1, 5, 3, 6, 4]
     *   return 5
     *
     *   prices = [7, 6, 4, 3, 1]
     *   return 0
     *
     * Constraints:
     * - 1 <= prices.length <= 100_000
     * - 0 <= prices[i] <= 10_000
     */
    public static int maximumProfit(int[] prices) {
        int max_profit =0;
       for(int i =0; i<prices.length-1;i++){
           for(int j =i+1;j<prices.length;j++ ){
               int current_profit = prices[j]-prices[i];
               if(current_profit>max_profit){
                   max_profit=current_profit;
               }
           }
       }
        return max_profit;
    }

    private static void runCase(
            String name,
            int[] prices,
            int expected) {
        int actual = maximumProfit(prices);
        boolean passed = expected == actual;

        System.out.println((passed ? "PASS" : "FAIL") + " - " + name);
        System.out.println("  expected: " + expected);
        System.out.println("  actual:   " + actual);
    }

    public static void main(String[] args) {
        runCase(
                "standard profitable trade",
                new int[] {7, 1, 5, 3, 6, 4},
                5);

        runCase(
                "steadily falling prices",
                new int[] {7, 6, 4, 3, 1},
                0);

        runCase(
                "single day",
                new int[] {5},
                0);

        runCase(
                "unchanged prices",
                new int[] {2, 2, 2, 2},
                0);

        runCase(
                "maximum price boundary",
                new int[] {0, 10_000},
                10_000);

        runCase(
                "best trade occurs late",
                new int[] {3, 8, 1, 9},
                8);

        runCase(
                "two day gain",
                new int[] {1, 2},
                1);
    }
}

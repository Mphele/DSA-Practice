package com.practice;

import java.util.Arrays;

public class TransposeMatrix {

    public static void main(String[] args) {
        int[][] initial = {
                {1, 2, 3},
                {4, 5, 6}
        };

        int[][] solution = transpose(initial);
        System.out.println(Arrays.deepToString(solution));
    }

    public static int[][] transpose(int[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;

        int[][] transposed = new int[cols][rows];

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                transposed[c][r] = matrix[r][c];
            }
        }

        return transposed;
    }
}
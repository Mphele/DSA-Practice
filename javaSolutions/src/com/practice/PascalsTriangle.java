package com.practice;

import java.util.ArrayList;
import java.util.List;

public class PascalsTriangle {

    public static void main(String[] args) {
        int numRows = 5;
        List<List<Integer>> solution = generate(numRows);
        System.out.println(solution);
    }

    public static List<List<Integer>> generate(int numRows) {

    List<List<Integer>> triangle = new ArrayList<>();

    triangle.add(List.of(1));

    for(int i =1; i<numRows;i++ ){

        List<Integer> prevRow = triangle.get(i-1);
        List<Integer> row = new ArrayList<>();

        row.add(1);

        for(int j =1; j<i; j++){

            row.add(prevRow.get(j-1)+ prevRow.get(j));

        }
        row.add(1);
        triangle.add(row);

    }

        return triangle;
    }
}
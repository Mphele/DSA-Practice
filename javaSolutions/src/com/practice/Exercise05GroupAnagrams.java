package com.practice;

import java.util.*;

public class Exercise05GroupAnagrams {

    /*
     * Exercise 05: Group Anagrams
     *
     * Source: https://leetcode.com/problems/group-anagrams/
     * Original difficulty: Medium
     *
     * Task:
     * Given an array of lowercase words, collect words made from the same
     * letters into groups. The groups and the words inside them may be
     * returned in any order.
     *
     * Examples:
     *   input:  ["eat", "tea", "tan", "ate", "nat", "bat"]
     *   output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
     *
     *   input:  [""]
     *   output: [[""]]
     *
     * Constraints:
     * - 1 <= words.length <= 10_000
     * - 0 <= words[i].length() <= 100
     * - Every word contains only lowercase English letters.
     */
    public static List<List<String>> groupAnagrams(String[] words) {

        Map<String, List<String>> sortToAnagrams = new HashMap<>();

        for(String word: words){
            String sortedWord = sortStr(word);

            if(!sortToAnagrams.containsKey(sortedWord)){
                sortToAnagrams.put(sortedWord,new ArrayList<>());
            }

            sortToAnagrams.get(sortedWord).add(word);

        }

        List<List<String>> anagramGroups = new ArrayList<>();

        for(String sorted: sortToAnagrams.keySet()){
            anagramGroups.add(sortToAnagrams.get(sorted));
        }

        return anagramGroups;

    }

    private static String sortStr(String word){
        char [] letters = word.toCharArray();
        Arrays.sort(letters);
        return String.valueOf(letters);
    }

    private static String canonicalize(List<List<String>> groups) {
        if (groups == null) {
            return "null";
        }

        List<String> normalizedGroups = new ArrayList<String>();
        for (List<String> group : groups) {
            List<String> normalizedWords = new ArrayList<String>(group);
            Collections.sort(normalizedWords);
            normalizedGroups.add(normalizedWords.toString());
        }
        Collections.sort(normalizedGroups);
        return normalizedGroups.toString();
    }

    private static void runCase(
            String name,
            String[] words,
            List<List<String>> expected) {
        List<List<String>> actual = groupAnagrams(words);
        String normalizedExpected = canonicalize(expected);
        String normalizedActual = canonicalize(actual);
        boolean passed = normalizedExpected.equals(normalizedActual);

        System.out.println((passed ? "PASS" : "FAIL") + " - " + name);
        System.out.println("  expected: " + normalizedExpected);
        System.out.println("  actual:   " + normalizedActual);
    }

    public static void main(String[] args) {
        runCase(
                "mixed groups",
                new String[] {"eat", "tea", "tan", "ate", "nat", "bat"},
                Arrays.asList(
                        Arrays.asList("eat", "tea", "ate"),
                        Arrays.asList("tan", "nat"),
                        Arrays.asList("bat")));

        runCase(
                "empty word",
                new String[] {""},
                Arrays.asList(Arrays.asList("")));

        runCase(
                "single word",
                new String[] {"a"},
                Arrays.asList(Arrays.asList("a")));

        runCase(
                "duplicate words",
                new String[] {"abc", "abc", "bca"},
                Arrays.asList(Arrays.asList("abc", "abc", "bca")));

        runCase(
                "several similarly sized groups",
                new String[] {"listen", "silent", "enlist", "rat", "tar", "art", "x"},
                Arrays.asList(
                        Arrays.asList("listen", "silent", "enlist"),
                        Arrays.asList("rat", "tar", "art"),
                        Arrays.asList("x")));
    }
}

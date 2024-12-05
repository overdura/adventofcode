package main.java.ovg.aoc2024;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

import main.java.ovg.aoc2024.common.Utils;

public class Day05 {
    private static final String INPUT_PATH = "src/main/resources/05.in";

    public static void main(String[] args) throws Exception {
        List<String> content = Utils.getDataFromFile(INPUT_PATH);

        List<String> rules = new ArrayList<>();
        List<String> pages = new ArrayList<>();

        for (String line: content) {
            if (line.contains("|")){
                rules.add(line);
            } else if (line.contains(",")) {
                pages.add(line);
            }
        }

        int result1 = 0;
        int result2 = 0;
        for (String pagesToPrint: pages) {
            result1 += getMiddlePageNumber(rules, pagesToPrint);
            result2 += getMiddlePageNumberPart2(rules, pagesToPrint);
        }

        Utils.printResult("--- Day 5: Print Queue ---", String.valueOf(result1), String.valueOf(result2));
    }

    private static int getMiddlePageNumber(List<String> rules, String updates) {

        List<String> updatePages = Arrays.asList(updates.split(","));
        boolean isValid = isValid(rules, updatePages);

        if (isValid) {
            return Integer.valueOf(updatePages.get(updatePages.size()/2));
        }

        return 0;
    }

    private static int getMiddlePageNumberPart2(List<String> rules, String updates) {

        List<String> updatePages = Arrays.asList(updates.split(","));
        
        boolean isValid = isValid(rules, updatePages);
        
        if (!isValid) {
            List<String> result = reorder(rules, updatePages);
            return Integer.valueOf(result.get(result.size()/2));
        }

        return 0;
    }

    private static boolean isValid(List<String> rules, List<String> updates) {
        boolean isValid = true;

        for (String rule: rules) {
            String[] pages = rule.split("\\|");
            
            if (updates.contains(pages[0]) && updates.contains(pages[1])){
                var firstPosition = updates.indexOf(pages[0]);
                var secondPosition = updates.indexOf(pages[1]);
                if (firstPosition>secondPosition) {
                    isValid = false;
                    break;
                }
            }
        }

        return isValid;
    }

    private static List<String>  reorder(List<String> rules, List<String> updates) {
        boolean isValid = true;

        for (String rule: rules) {
            String[] pages = rule.split("\\|");
            
            if (updates.contains(pages[0]) && updates.contains(pages[1])){
                var firstPosition = updates.indexOf(pages[0]);
                var secondPosition = updates.indexOf(pages[1]);
                if (firstPosition>secondPosition) {

                    // alternative -> //Collections.swap(updates, firstPosition, secondPosition);
                    String temp = updates.get(firstPosition);
                    updates.set(firstPosition, updates.get(secondPosition));
                    updates.set(secondPosition, temp);
                    
                    isValid = false;
                    break;
                }
            }
        }

        if (!isValid) {
            return reorder(rules, updates);
        }

        return updates;
    }

}

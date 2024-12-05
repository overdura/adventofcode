package main.java.ovg.aoc2024;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

import main.java.ovg.aoc2024.common.Utils;

public class Day02 {
    private static final String INPUT_PATH = "src/main/resources/02.in";

    public static void main(String[] args) throws Exception {
        List<String> content = Utils.getDataFromFile(INPUT_PATH);

        int result1 = 0;
        int result2 = 0;

        for (String line : content) {
            var report = convertToReport(line);

            if (isSafe(report)) {
                result1++;
                result2++;
            } else if (isSafePart2(report)) {
                result2++;
            }
        }

        Utils.printResult("--- Day 2: Red-Nosed Reports ---", String.valueOf(result1), String.valueOf(result2));
    }

    private static List<Integer> convertToReport(String row) {
        return Arrays.stream(row.split("\\s+"))
                .filter(s -> !s.isEmpty())
                .map(Integer::parseInt)
                .collect(Collectors.toList());
    }

    private static boolean isSafe(List<Integer> report) {
        var sorted = new ArrayList<>(report);
        Collections.sort(sorted);
        var sortedReversed = new ArrayList<>(report);
        Collections.sort(sortedReversed, Collections.reverseOrder());

        if (report.equals(sorted) || report.equals(sortedReversed)) {
            for (int i = 0; i < report.size() - 1; i++) {
                int difference = report.get(i) - report.get(i + 1);
                if (Math.abs(difference) < 1 || Math.abs(difference) > 3) {
                    return false;
                }
            }
            return true;
        }
        return false;
    }

    private static boolean isSafePart2(List<Integer> report) {
        for (int i = 0; i < report.size(); i++) {
            List<Integer> withoutLevel = new ArrayList<>(report);
            withoutLevel.remove(i);
            if (isSafe(withoutLevel)) {
                return true;
            }
        }
        return false;
    }

}

package main.java.ovg.aoc2024;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

import main.java.ovg.aoc2024.common.Utils;

public class Day01 {
    private static final String INPUT_PATH = "src/main/resources/01.in";

    public static void main(String[] args) throws Exception {
        List<String> content = Utils.getDataFromFile(INPUT_PATH);

        var left = new ArrayList<Integer>();
        var right = new ArrayList<Integer>();

        content.stream()
                .forEach(row -> {
                    String[] point = row.split("   ");
                    left.add(Integer.parseInt(point[0]));
                    right.add(Integer.parseInt(point[1]));
                });

        List<Integer> sortedLeft = left.stream().sorted().collect(Collectors.toList());
        List<Integer> sortedRight = right.stream().sorted().collect(Collectors.toList());

        int result1 = 0;
        int result2 = 0;

        for (int i = 0; i < sortedLeft.size(); i++) {
            var leftElement = sortedLeft.get(i);
            var rightElement = sortedRight.get(i);

            result1 += Math.abs(rightElement - leftElement);

            long countLeftInRight = sortedRight.stream()
                    .filter(el -> el.equals(leftElement))
                    .count();
            result2 += leftElement * countLeftInRight;
        }

        Utils.printResult("DAY 1", String.valueOf(result1), String.valueOf(result2));
    }

}

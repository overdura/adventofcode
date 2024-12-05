package main.java.ovg.aoc2024;

import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import main.java.ovg.aoc2024.common.Utils;

public class Day03 {
    private static final String INPUT_PATH = "src/main/resources/03.in";

    public static void main(String[] args) throws Exception {
        List<String> content = Utils.getDataFromFile(INPUT_PATH);

        var totalContent = "";

        for (String line : content) {
            totalContent += line;
        }
        int result1 = calculate(totalContent);
        int result2 = calculatePart2(totalContent);

        Utils.printResult("--- Day 3: Mull It Over ---", String.valueOf(result1), String.valueOf(result2));
    }

    private static int calculate(String content) {
        var result = 0;

        String regex = "mul\\((\\d+),(\\d+)\\)";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(content);

        while (matcher.find()) {
            String match = matcher.group();
            var operation = match.replace("mul(", "").replace(")", "").split(",");
            var first = Integer.parseInt(operation[0]);
            var second = Integer.parseInt(operation[1]);
            result += first * second;
        }
        return result;
    }

    private static int calculatePart2(String content) {
        int result = 0;

        String regex = "(don't\\(\\)|do\\(\\))";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(content);
        boolean enabled = true;
        String data = "";
        int ixSeparator = 0;

        while (matcher.find()) {
            data = content.substring(ixSeparator, matcher.start());
            String separator = matcher.group();

            if (enabled) {
                result += calculate(data);
            }

            enabled = separator.contains("don") ? false : true;

            ixSeparator = matcher.end();
        }
        if (enabled) {
            result += calculate(content.substring(ixSeparator, content.length()));
        }
        return result;
    }

}

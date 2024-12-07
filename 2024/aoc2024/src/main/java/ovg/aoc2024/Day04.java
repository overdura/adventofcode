package main.java.ovg.aoc2024;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

import main.java.ovg.aoc2024.common.Utils;

public class Day04 {
    private static final String INPUT_PATH = "src/main/resources/04.in";

    public static void main(String[] args) throws Exception {
        List<String> content = Utils.getDataFromFile(INPUT_PATH);

        int result1 = calculateInLine(content);
        result1 += calculateInLine(transpose(content));

        var matrix = Utils.getMatrix(content);
        result1 += calculateDiagonal(matrix);

        int result2 = calculateXMas(matrix);
        result2 += calculateXMas(transposeMatrix(matrix));

        Utils.printResult("--- Day 4: Ceres Search---", String.valueOf(result1), String.valueOf(result2));
    }

    private static int calculateInLine(List<String> content) {
        var result = 0;

        String regex = "XMAS";
        Pattern pattern = Pattern.compile(regex);
        for (String line : content) {
            Matcher matcher = pattern.matcher(line);

            while (matcher.find()) {
                result++;
            }
        }

        regex = "SAMX";
        pattern = Pattern.compile(regex);
        for (String line : content) {
            Matcher matcher = pattern.matcher(line);

            while (matcher.find()) {
                result++;
            }
        }
        return result;
    }

    private static List<String> transpose(List<String> content) {
        int numCols = content.get(0).length();

        List<StringBuilder> columns = new ArrayList<>();
        for (int i = 0; i < numCols; i++) {
            columns.add(new StringBuilder());
        }

        for (String row : content) {
            for (int i = 0; i < row.length(); i++) {
                columns.get(i).append(row.charAt(i));
            }
        }

        return columns.stream()
                .map(StringBuilder::toString)
                .collect(Collectors.toUnmodifiableList());
    }

    private static int calculateDiagonal(char[][] content) {
        int result = 0;

        // pattern: XMAS or SAMX
        int rows = content.length;
        int columns = content[0].length;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns - 3; j++) {
                // _/
                if (i > 2) {
                    if ((content[i][j] == 'X' && content[i - 1][j + 1] == 'M' && content[i - 2][j + 2] == 'A'
                            && content[i - 3][j + 3] == 'S')
                            || (content[i][j] == 'S' && content[i - 1][j + 1] == 'A' && content[i - 2][j + 2] == 'M'
                                    && content[i - 3][j + 3] == 'X')) {
                        result++;
                    }
                }
                // -\
                if (i < rows - 3) {
                    if ((content[i][j] == 'X' && content[i + 1][j + 1] == 'M' && content[i + 2][j + 2] == 'A'
                            && content[i + 3][j + 3] == 'S')
                            || (content[i][j] == 'S' && content[i + 1][j + 1] == 'A' && content[i + 2][j + 2] == 'M'
                                    && content[i + 3][j + 3] == 'X')) {
                        result++;
                    }
                }
            }
        }

        return result;
    }

    private static int calculateXMas(char[][] content) {
        int result = 0;
        int rows = content.length;
        int columns = content[0].length;

        // M.S S.M
        // .A. .A.
        // M.S S.M
        for (int i = 1; i < rows - 1; i++) {
            for (int j = 1; j < columns - 1; j++) {
                if (content[i][j] == 'A') {
                    if ((content[i - 1][j - 1] == 'M' && content[i - 1][j + 1] == 'S')
                            && (content[i + 1][j - 1] == 'M' && content[i + 1][j + 1] == 'S')) {
                        result++;
                    } else if ((content[i - 1][j - 1] == 'S' && content[i - 1][j + 1] == 'M')
                            && (content[i + 1][j - 1] == 'S' && content[i + 1][j + 1] == 'M')) {
                        result++;
                    }
                }
            }
        }
        return result;
    }

    private static char[][] transposeMatrix(char[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;

        char[][] result = new char[cols][rows];

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                result[j][i] = matrix[i][j];
            }
        }

        return result;
    }

}

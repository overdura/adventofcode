package main.java.ovg.aoc2024.common;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class Utils {
    public static List<String> getDataFromFile(String filePath) {
        try {
            return Files.readAllLines(Paths.get(filePath));
        } catch (IOException io) {
            System.out.println("file can't read");
            return List.of();
        }
    }

    public static void printResult(String day, String result1, String result2) {
        System.out.println("\n--");
        System.out.println(day);
        System.out.println("--");
        System.out.println("part 1: " + result1);
        System.out.println("part 2: " + result2);
        System.out.println("--\n");
    }

}

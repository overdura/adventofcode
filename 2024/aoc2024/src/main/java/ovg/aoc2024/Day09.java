package main.java.ovg.aoc2024;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import main.java.ovg.aoc2024.common.Utils;

public class Day09 {
    private static final String INPUT_PATH = "src/main/resources/09.in";

    // 1408072414 low
    public static void main(String[] args) throws Exception {
        List<String> content = Utils.getDataFromFile(INPUT_PATH);

        char[] diskMap = content.get(0).toCharArray();

        List<String> blocks = convertToBlocks(diskMap);
        List<String> compactIndividualBlocks = compact(blocks);
        long result1 = getChecksum(compactIndividualBlocks);
        long result2 = 0;

        Utils.printResult("--- Day 9: Disk Fragmenter ---", String.valueOf(result1), String.valueOf(result2));
    }

    private static List<String> convertToBlocks(char[] diskMap) {
        List<String> result = new ArrayList<>();

        int blockNumber = 0;
        for (int i = 0; i < diskMap.length; i++) {
            var block = ".";
            int elements = Character.getNumericValue(diskMap[i]);
            if (i % 2 == 0) { // block
                block = String.valueOf(blockNumber);
                blockNumber++;
            }
            for (int j = 0; j < elements; j++) {
                result.add(block);
            }
        }
        return result;
    }

    private static List<String> compact(List<String> blocks) {
        List<String> result = new ArrayList<>(blocks);

        int ini = 0;
        int end = blocks.size() - 1;
        for (String el : blocks) {
            if (el.equals(".")) {
                for (int j = end; j >= ini; j--) {
                    if (!blocks.get(j).equals(".")) {
                        Collections.swap(result, ini, j);
                        end--;
                        break;
                    } else {
                        end--;
                    }
                }
            }
            ini++;
        }
        return result;
    }

    private static long getChecksum(List<String> arr) {
        long result = 0;
        long i = 0;
        for (String el : arr) {
            if (!el.equals(".")) {
                // arr.indexOf is slow vs i counter
                result += i * Long.valueOf(el);
            }
            i++;
        }
        return result;
    }

}

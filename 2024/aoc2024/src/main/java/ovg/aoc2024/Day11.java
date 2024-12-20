package main.java.ovg.aoc2024;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import main.java.ovg.aoc2024.common.Utils;

public class Day11 {
    public static void main(String[] args) throws Exception {
        List<Long> stones = List.of(554735l, 45401l, 8434l, 0l, 188l, 7487525l, 77l, 7l);
        // List<Long> stones = List.of(125l, 17l); // test

        long ini1 = System.currentTimeMillis();
        long result1 = calculateStonesByBlink(stones, 25);
        long end1 = System.currentTimeMillis();

        long ini2 = System.currentTimeMillis();
        long result2 = calculateStonesByBlinkOptimized(stones, 75);
        long end2 = System.currentTimeMillis();

        System.out.println("\nt1 -> " + (end1 - ini1));
        System.out.println("t2 -> " + (end2 - ini2));

        Utils.printResult("--- Day 11: Plutonian Pebbles ---", String.valueOf(result1), String.valueOf(result2));
    }

    private static int calculateStonesByBlink(List<Long> stones, int blinks) {
        List<Long> result = new ArrayList<>(stones);
        for (int i = 0; i < blinks; i++) {
            result = transform(result);
        }
        return result.size();
    }

    private static List<Long> transform(List<Long> stones) {
        List<Long> result = new ArrayList<>();
        for (Long stone : stones) {
            if (stone == 0) {
                result.add(1l);
            } else if (stone == 1) {
                result.add(2024l);
            } else if (String.valueOf(stone).length() % 2 == 0) {
                String stoneString = String.valueOf(stone);
                int middle = stoneString.length() / 2;
                long numberValue = Long.valueOf(stoneString.substring(0, middle));
                result.add(numberValue);
                numberValue = Long.valueOf(stoneString.substring(middle));
                result.add(numberValue);
            } else {
                result.add(2024l * stone);
            }
        }
        return result;
    }

    private static long calculateStonesByBlinkOptimized(List<Long> stones, int blinks) {
        Map<Long, Long> result = new HashMap<>();
        for (Long stone : stones) {
            result.put(stone, 1l);
        }

        for (int i = 0; i < blinks; i++) {
            result = transformOptimized(result);
        }

        return result.values().stream().mapToLong(Long::longValue).sum();
    }

    private static Map<Long, Long> transformOptimized(Map<Long, Long> stones) {
        Map<Long, Long> result = new HashMap<>();

        stones.forEach((stoneKey, count) -> {
            List<Long> transformations = new ArrayList<>();
            if (stoneKey == 0L) {
                transformations.add(1L);
            } else if (stoneKey == 1L) {
                transformations.add(2024L);
            } else if (String.valueOf(stoneKey).length() % 2 == 0) {
                String keyString = String.valueOf(stoneKey);
                int middle = keyString.length() / 2;
                long firstPart = Long.parseLong(keyString.substring(0, middle));
                long secondPart = Long.parseLong(keyString.substring(middle));
                transformations.add(firstPart);
                transformations.add(secondPart);
            } else {
                transformations.add(2024L * stoneKey);
            }

            for (Long transformedKey : transformations) {
                result.put(transformedKey, result.getOrDefault(transformedKey, 0L) + count);
            }
        });
        return result;
    }

}

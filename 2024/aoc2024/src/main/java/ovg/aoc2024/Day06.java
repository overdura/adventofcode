package main.java.ovg.aoc2024;

import java.util.ArrayList;
import java.util.List;

import main.java.ovg.aoc2024.common.Utils;

public class Day06 {
    private static final String INPUT_PATH = "src/main/resources/06.in";

    public static void main(String[] args) throws Exception {
        List<String> content = Utils.getDataFromFile(INPUT_PATH);

        var matrixMap = Utils.getMatrix(content);
        var initialCoords = getInitialGuardPosition(matrixMap);
        int result1 = calculateTotalPositions(matrixMap, initialCoords);

        int result2 = 0;
        
        Utils.printResult("--- Day 6: Guard Gallivant ---", String.valueOf(result1), String.valueOf(result2));
    }

    private static void printMatrix(char[][] matrix) {
        for (char[] row : matrix) {
            for (char ch : row) {
                System.out.print(ch);
            }
            System.out.println();
        }
    }

    private static Point getInitialGuardPosition(char[][] matrix) {
        var rows = matrix.length;
        var cols = matrix[0].length;

        for (int i = 0; i<rows; i++) {
            for (int j= 0; j<cols; j++) {
                if (matrix[i][j] == '^') {
                    return new Point(i, j);
                    
                }
            }
        }
        return new Point(0, 0);
    }

    private static int calculateTotalPositions(char[][] matrix, Point init) {
        int result = 1;
        int rows = matrix.length;
        int cols = matrix[0].length;

        char[][]steps = matrix;

        var position = init;
        var direction = '^';
        List<Point> visited = new ArrayList<>();
        visited.add(init);

        while ((position.x >= 0 || position.x <= rows) && (position.y >= 0 || position.y <= cols)) {
            //System.err.println(result+ " " + direction + " " + position);

            if (!visited.contains(position)){
                visited.add(position);
                result++;
            }

            if (direction == '^') {
                position = new Point(position.x - 1, position.y);
                if (position.x <0 || position.x > rows-1) {
                    break;
                }
                
                if (matrix[position.x][position.y] == '#') {
                    direction = '>';
                    position = new Point(position.x + 1, position.y);
                }
  
            }
            
            if (direction == '>') {
                position = new Point(position.x, position.y+1);
                if (position.y <0 || position.y > cols-1) {
                    break;
                }
                if (matrix[position.x][position.y] == '#') {
                    direction = 'v';
                    position = new Point(position.x, position.y-1);
                }
            }
            if (direction == 'v') {
                position = new Point(position.x + 1, position.y);
                if (position.x <0 || position.x > rows-1) {
                    break;
                }
                if (matrix[position.x][position.y] == '#') {
                    direction = '<';
                    position = new Point(position.x - 1, position.y);
                }
            }
            if (direction == '<') {
                position = new Point(position.x, position.y-1);
                if (position.y <0 || position.y > cols-1) {
                    break;
                }
                if (matrix[position.x][position.y] == '#') {
                    direction = '^';
                    position = new Point(position.x, position.y+1);

                }
            }
  

        }

        //printMatrix(steps);
        return result;
    }

    record Point(int x, int y) {}
}

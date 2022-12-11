import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Resolve {
    
    private static final String DATA_PATH = "data.in";

    public static void main(String[] args) throws Exception{
        System.out.println("Resolving problem...");
        partOne();
        partTwo();
    }


    private static BufferedReader getFileData() throws FileNotFoundException{
        System.out.println(  System.getProperty("user.dir"));
        return new BufferedReader(new FileReader(Resolve.class.getClassLoader().getResource("").getPath()+DATA_PATH));
    }

    private static void partOne() throws IOException {
        System.out.println("Problem one");
        var data = getFileData();

        String line = data.readLine();
        int totalCalories = 0;
        int actualCalories = 0;
        while(line != null) {
            if (line.equals("")) {
                if (actualCalories > totalCalories) {
                    totalCalories = actualCalories;
                }
                actualCalories = 0;

            } else {
                actualCalories += Integer.parseInt(line);
            }
            line = data.readLine();
        }

        System.out.println("Total calories: " + totalCalories);

    }

    private static void partTwo() throws IOException {
        System.out.println("Problem two");
        var data = getFileData();

        List<Integer> totalCalories = new ArrayList<>();
        int actualCalories = 0;
        String line = data.readLine();

        while(line != null) {
            if (line.equals("")) {
                totalCalories.add(actualCalories);
                actualCalories = 0;

            } else {
                actualCalories += Integer.parseInt(line);
            }
            line = data.readLine();
        }

        Collections.sort(totalCalories, Collections.reverseOrder());
        System.out.println("Total calories: " + (totalCalories.get(0) + totalCalories.get(1) + totalCalories.get(2)));

    }
}
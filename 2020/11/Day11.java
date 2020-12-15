import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

public class Day11 {
    final static char EMPTY = 'L';
    final static char OCCUPIED = '#';
    final static char FLOOR = '.';

    public static int countOccupiedAdj(int x, int y, List<String> grid) {
        int[] xs = new int[] {x-1, x, x+1};
        int[] ys = new int[] {y-1, y, y+1};
        
        int count = 0;
        for (int tx : xs) {
            if (tx < 0 || tx >= grid.get(0).length())
                continue;
            for (int ty : ys) {
                if (ty < 0 || ty >= grid.size()) 
                    continue;
                if (ty == y && tx == x)
                    continue;
                count += grid.get(ty).charAt(tx) == OCCUPIED ? 1 : 0;
            } 
        }
        return count;
    }

    public static int charCount(String s, char t) {
        int count = 0;
        for (int i = 0; i < s.length(); ++i) {
            if (s.charAt(i) == t) ++count;
        }
        return count;
    }

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        List<String> grid = new ArrayList<>(70);
        while(s.hasNextLine()) {
            grid.add(s.nextLine()); 
        }


        int iters = 0;
        int numChanges = 0;
        do {
            List<String> newGrid = new ArrayList<>(grid.size());
            numChanges = 0;

            for (int y = 0; y < grid.size(); ++y) {
                String newRow = "";
                for (int x = 0; x < grid.get(y).length(); ++x) {
                    char current = grid.get(y).charAt(x);
                    int adj = countOccupiedAdj(x,y,grid);
                    if (current == EMPTY && adj == 0) {
                        current = OCCUPIED;
                        ++numChanges;
                    } else if (current == OCCUPIED && adj >= 4) {
                        current = EMPTY;
                        ++numChanges;
                    }
                    newRow += current;
                }
                assert newRow.length() == grid.get(y).length();
                newGrid.add(newRow);
            }
            assert grid.size() == newGrid.size();

            grid = newGrid;
            ++iters; 
        } while(numChanges > 0);

        System.out.println(iters);
        System.out.println(grid.stream()
                .map(x -> charCount(x, OCCUPIED))
                .reduce(0, Integer::sum));
    }
}

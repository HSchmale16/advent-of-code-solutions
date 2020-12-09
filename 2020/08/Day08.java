import java.util.*;

class Op {
    public String action;
    public final int value;

    public Op(String action, int value) {
        this.action = action;
        this.value = value; 
    }
}

public class Day08 {
    // { acc value, term reason }
    // term reason in 1 for killed by loop.
    // term reaon in 0 for killed by going past valid pc
    public static int[] runIt(List<Op> ops) {
        int acc = 0;
        int programCounter = 0;
        Set<Integer> seenProgCounters = new HashSet<>();

        // start by assuming we are gonna die by infinite loop
        int termReason = 1;
        try {
            while (!seenProgCounters.contains(programCounter)) {
                seenProgCounters.add(programCounter);

                Op op = ops.get(programCounter);

                if (op.action.equals("jmp")) {
                    programCounter += op.value;
                    continue;
                }
                if (op.action.equals("acc")) {
                    acc += op.value;
                }
                ++programCounter;
            }
        } catch(IndexOutOfBoundsException e) {
            // we died bc no instruction there meaning it stopped
            termReason = 0;
        }
        return new int[]{acc, termReason};
    }

    // acc -> acc
    // nop -> jmp
    // jmp -> nop
    public static String invertAction(String action) {
        switch(action) {
            case "acc":
                return "acc";
            case "nop":
                return "jmp";
            case "jmp":
                return "nop";
        }
        return ""; 
    }

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        List<Op> ops = new ArrayList<>(1000);
        while(s.hasNextLine()) {
            String line = s.nextLine();
            String[] parts = line.split(" ");
            ops.add(new Op(parts[0], Integer.valueOf(parts[1])));
        }

        int[] result = runIt(ops);
        System.out.println("Part 1: " + result[0]);

        System.out.println(result[1]);
        // For part 2
        for (int i = 0; i < ops.size() && result[1] > 0; ++i) {
            Op op = ops.get(i);
            if (op.action.startsWith("a"))
                continue;
            
            op.action = invertAction(op.action);
            result = runIt(ops);
            if (result[1] == 0) {
                System.out.println("Part 2: " + result[0]);
            }
            op.action = invertAction(op.action); 
        } 
    }
}

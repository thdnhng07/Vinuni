package Lab7;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class StackStutter {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        List<Integer> inputList = new ArrayList<>();

        while (input.hasNextLine()) {
            String line = input.nextLine().trim();
            if (line.equals("#")) break;
            inputList.add(Integer.parseInt(line));
        }
        System.out.println("Original stack: " + inputList);
        Stack<Integer> stutteredStack = new Stack<>();

        for (int num : inputList) {
            stutteredStack.push(num);
            stutteredStack.push(num);
        }
        List<Integer> outputList = new ArrayList<>();
        Stack<Integer> tempoStack = new Stack<>();

        while (!stutteredStack.isEmpty()) {
            tempoStack.push(stutteredStack.pop());
        }

        while (!tempoStack.isEmpty()) {
            outputList.add(tempoStack.pop());
        }
        System.out.println("Stack after stutter: " + outputList);
    }
}

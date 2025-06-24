import java.util.*;

public class Main {
    static int computeScore(int[] arr) {
        int n = arr.length;
        int[] leftSecondMin = new int[n];
        int[] rightSecondMin = new int[n];
        final int INF = Integer.MAX_VALUE;

        // Compute second minimum from the left
        int min1 = INF, min2 = INF;
        for (int i = 0; i < n; i++) {
            leftSecondMin[i] = min2;
            if (arr[i] < min1) {
                min2 = min1;
                min1 = arr[i];
            } else if (arr[i] < min2) {
                min2 = arr[i];
            }
        }

        // Compute second minimum from the right
        min1 = INF;
        min2 = INF;
        for (int i = n - 1; i >= 0; i--) {
            rightSecondMin[i] = min2;
            if (arr[i] < min1) {
                min2 = min1;
                min1 = arr[i];
            } else if (arr[i] < min2) {
                min2 = arr[i];
            }
        }

        // Calculate the total score
        int score = 0;
        for (int i = 0; i < n; i++) {
            int a = leftSecondMin[i];
            int b = rightSecondMin[i];
            int power = Math.max(arr[i] - a, arr[i] - b);
            score += power;
        }

        return score;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = Integer.parseInt(scanner.nextLine().trim());
        int[] arr = Arrays.stream(scanner.nextLine().trim().split(" "))
                          .mapToInt(Integer::parseInt)
                          .toArray();
        int result = computeScore(arr);
        System.out.println(result);
    }
}

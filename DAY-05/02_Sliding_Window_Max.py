import java.util.*;

public class Main {
    public static List<Integer> find_tallest(int N, int K, List<Integer> height) {
        List<Integer> result = new ArrayList<>();
        Deque<Integer> deque = new ArrayDeque<>();

        for (int i = 0; i < N; i++) {
            // Remove indices that are out of this window
            while (!deque.isEmpty() && deque.peekFirst() <= i - K) {
                deque.pollFirst();
            }

            // Remove indices whose corresponding values are less than height[i]
            while (!deque.isEmpty() && height.get(deque.peekLast()) < height.get(i)) {
                deque.pollLast();
            }

            // Add current index
            deque.offerLast(i);

            // Add to result from K-1 onwards
            if (i >= K - 1) {
                result.add(height.get(deque.peekFirst()));
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        List<Integer> height = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            height.add(sc.nextInt());
        }
        List<Integer> result = find_tallest(N, K, height);
        for (int i : result) {
            System.out.print(i + " ");
        }
        System.out.println();
    }
}

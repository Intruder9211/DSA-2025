//by using sliding window technique
import java.util.*;

public class Main {
    
    public static List<Integer> getSubarrayBeauty(List<Integer> nums, int k, int x) {
        List<Integer> result = new ArrayList<>();

        // -50 to 50 ke beech values hain, to frequency array le lete hain size 101
        int[] freq = new int[101];

        // Pehle k elements ke liye frequency count kar lo
        for (int i = 0; i < k; i++) {
            int val = nums.get(i);
            if (val < 0) freq[val + 50]++;
        }

        // Function to find xth smallest negative number
        result.add(findXthNegative(freq, x));

        for (int i = k; i < nums.size(); i++) {
            int out = nums.get(i - k);
            int in = nums.get(i);

            // Window se ek bahar nikal raha hai
            if (out < 0) freq[out + 50]--;

            // Naya element window mein aa raha hai
            if (in < 0) freq[in + 50]++;

            // Current window ke liye xth smallest negative dhoondo
            result.add(findXthNegative(freq, x));
        }

        return result;
    }

    // xth smallest negative number dhoondhne ke liye function
    public static int findXthNegative(int[] freq, int x) {
        int count = 0;
        for (int i = 0; i < 50; i++) { // -50 se -1 (index 0 to 49)
            count += freq[i];
            if (count >= x) return i - 50; // i - 50 se actual number milega
        }
        return 0; // agar x negative elements nahi mile
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input lena
        int k = scanner.nextInt(); // Subarray size
        int x = scanner.nextInt(); // Kaunsa x-th negative number chahiye
        int n = scanner.nextInt(); // Total elements
        List<Integer> nums = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            nums.add(scanner.nextInt());
        }

        // Function call
        List<Integer> result = getSubarrayBeauty(nums, k, x);

        // Output print karna
        for (int val : result) {
            System.out.print(val + " ");
        }
    }
}

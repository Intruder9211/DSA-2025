import java.util.*;

public class Main {
    public static int maxSumAfterPartitioning(int[] arr, int k) {
        // Write your logic here.
        int n = arr.length;
        int[] dp = new int[n+1];
        for(int i = 1; i <=n; i++){
            int maxInPartition=0;
            for (int j=1; j<=k && i-j >=0; j++){
                maxInPartition= Math.max(maxInPartition, arr[i-j]);
                dp[i] = Math.max(dp[i], dp[i-j] + maxInPartition*j);
            }
        }
        return dp[n];
    }

    public static int sieveOfEratosthenes(int n) {
        // Write your logic here.
        if(n<2) return 0;
        boolean[] isPrime = new boolean[n+1];
        Arrays.fill(isPrime, true);
        isPrime[0] = false;
        isPrime[1] = false;

        for(int i=2; i*i <=n; i++){
            if(isPrime[i]){
                for (int j=i*i; j<=n; j+=i)
                isPrime[j] = false;
            }
        }
        int count=0;
        for(boolean b: isPrime)
        if (b) count++;
        return count;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
        }
        int k = scanner.nextInt();
        
        // Call user logic functions
        int maxSum = maxSumAfterPartitioning(arr, k);
        int primeCount = sieveOfEratosthenes(maxSum);
        
        // Print the result
        System.out.println(primeCount);
    }
}

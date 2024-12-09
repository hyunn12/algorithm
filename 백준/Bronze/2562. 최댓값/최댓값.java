import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int[] temp = new int[9];
        
        for (int i = 0; i < 9; i++) {
            temp[i] = sc.nextInt();
        }

        int max = 1;

        for (int i = 0; i < 9; i++) {
            if (temp[i] > temp[max-1]) {
                max = i+1;
            }
        }

        System.out.println(Arrays.stream(temp).max().getAsInt());
        System.out.println(max);

    }

}
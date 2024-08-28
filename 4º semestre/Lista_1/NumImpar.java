import java.util.*;

public class NumImpar{
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int fistNumber = 0, laco, lastNumber = 0, imparNumber = 0, Number;
        laco = 0;
        do { 
            System.out.println("Insira um numero: ");
            Number = in.nextInt();
            laco++;
            if(Number % 2 == 1){
                imparNumber++;
                if(imparNumber == 1){
                    fistNumber = Number;
                }else if(imparNumber == 5){
                    lastNumber = Number;
                }
            }
            
        } while (imparNumber < 5);
        System.out.println("O primeiro numero eh: " + fistNumber);
        System.out.println("O ultimo numero eh: " + lastNumber );
        System.out.println("O numbero de vezes foi: " + laco);
    }
}
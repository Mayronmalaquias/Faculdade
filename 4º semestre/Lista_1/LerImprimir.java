import java.util.*;

public class LerImprimir{
    public static void main(String[] args){
        int i = 1;
        do { 
            Scanner in = new Scanner(System.in);
            System.out.println("Insira seu nome");
            String nome = in.nextLine();
            System.out.println("Seu nome é " + nome);
            i++;

        } while (i < 4);
    }
}
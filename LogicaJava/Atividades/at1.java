import java.util.Scanner;

public class at1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o primeiro número: ");
        double n1 = scanner.nextDouble();

        System.out.print("Digite o segundo número: ");
        double n2 = scanner.nextDouble();

        System.out.print("Digite o terceiro número: ");
        double n3 = scanner.nextDouble();

        double media = (n1 + n2 + n3) / 3;
        System.out.println("Média aritmética: " + media);

        scanner.close();
    }
}
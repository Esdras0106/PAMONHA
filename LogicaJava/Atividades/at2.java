import java.util.Scanner;

public class at2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite a força aplicada (F): ");
        double forca = scanner.nextDouble();

        System.out.print("Digite a distância percorrida (D): ");
        double distancia = scanner.nextDouble();

        double trabalho = forca * distancia;
        System.out.println("Trabalho realizado: " + trabalho);

        scanner.close();
    }
}
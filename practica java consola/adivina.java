import java.util.Random;
import java.util.Scanner;

public class adivina {

    public static void main(String[] args) {
        char[] letras = {'a', 'e', 'i', 'o', 'u'};
        Random rand = new Random();
        char letraAleatoria = letras[rand.nextInt(letras.length)];
        boolean adivinado = false;
        Scanner scanner = new Scanner(System.in);

        System.out.println("¡Bienvenido a Adivina la Letra!");
        System.out.println("Estoy pensando en una letra de las vocales. ¡Adivina cuál es!");

        while (!adivinado) {
            char letra = scanner.next().charAt(0);
            if (letra == letraAleatoria) {
                System.out.println("¡Adivinaste!");
                adivinado = true;
            } else {
                System.out.println("Incorrecto. Intenta de nuevo.");
            }
        }

        scanner.close();
    }
}

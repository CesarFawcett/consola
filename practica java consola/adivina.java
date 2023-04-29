import java.util.Random;
import java.util.Scanner;

public class adivina {

    public static void main(String[] args) {
        char[] letras = {'a', 'e', 'i', 'o', 'u'};
        Random rand = new Random();
        char letraAleatoria = letras[rand.nextInt(letras.length)];
        boolean adivinado = false;
        Scanner scanner = new Scanner(System.in);
        int cont = 1;

        System.out.println("¡Bienvenido a Adivina la Letra!");
        System.out.println("Estoy pensando en una letra vocal. ¡Adivina cuál es!, tienes 3 intentos :D");

        while (!adivinado && cont!=4) {
            char letra = scanner.next().charAt(0);
            if (letra == letraAleatoria) {
                System.out.println("¡Adivinaste!");
                adivinado = true;
            } else {
                System.out.println("Incorrecto. Intenta de nuesvo.");
                cont = cont + 1;
            }
        }
        System.out.println("La vocal era : "+letraAleatoria);
        scanner.close();
    }
}

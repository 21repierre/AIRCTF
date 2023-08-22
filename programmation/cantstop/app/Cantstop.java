import java.util.Random;
import java.util.Scanner;
import java.lang.NumberFormatException;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;

public class Cantstop {

    public static void main(String... args) {

        Random random = new Random();
        Scanner sc = new Scanner(System.in);
        int fortune = 10;

        System.out.println("Votre ami vous a parlé de ce nouveau jeu de hasard à la mode:");
        System.out.println("Une fleche est lancée sur elle-même et vous devez prédire dans quelle moitié cette dernière s'arrêtera.");
        System.out.println("Mais prenez garde, vous n'avez pas eu de nouvelles de lui depuis ce moment, il semble être tomber dans l'addiction.");
        System.out.println("Alors, arriverez-vous à vous arrêter ?");

        while (true) {
            if(fortune > 10000) {
                break;
            }
            System.out.println("Vous vous apprêtez à miser la moitié de votre fortune (" + fortune + ")");
            System.out.println("Mais que choisirez-vous? Avant le milieu ? Après ?");
            String line = sc.nextLine();
            boolean avant = false;
            if (line.equalsIgnoreCase("avant")) avant = true;
            else if (!line.equalsIgnoreCase("apres")) continue;
            double value = random.nextDouble();
            System.out.println("...et la fleche s'arrête sûr " + value + "!");
            if (value > 0.5 && !avant || value <= 0.5 && avant) {
                System.out.println("BRAVO! Vous doublez votre mise!");
                fortune += fortune / 2;
            } else {
                System.out.println("Vous perdez malheureusement votre mise.");
                fortune -= fortune / 2;
            }
        }
        
        try {
            BufferedReader reader = new BufferedReader(new FileReader("flag.txt"));
            String currentLine = reader.readLine();
            reader.close();

            System.out.println("Voyant la colossale fortune que vous avez amasse, le casino vous implore de vous arrêter.");
            System.out.println("Pour vous convaincre, le directeur vous tend ceci:" + currentLine);
        } catch (IOException e) {

        }
    }

}
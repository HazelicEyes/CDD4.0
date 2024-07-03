package aula6_string;

import java.util.Scanner;
import java.util.StringTokenizer;

public class exercicio15 {

	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		System.out.println("Digite seu texto: ");
		String texto = entrada.nextLine();
		StringTokenizer palavras = new StringTokenizer(texto);
		System.out.printf("O texto contem: " + palavras.countTokens() + " palavras");

	}

}

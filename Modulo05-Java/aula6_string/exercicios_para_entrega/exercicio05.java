package exercicios_para_entrega;

import java.util.Scanner;

public class exercicio05 {

	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		System.out.println("Digite seu texto: ");
		String texto = entrada.nextLine();
		String texto2 = texto.toUpperCase();
		System.out.println(texto2);

	}

}

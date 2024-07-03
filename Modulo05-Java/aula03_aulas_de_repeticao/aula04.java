package aula03_aulas_de_repeticao;

import java.util.Scanner;

public class aula04 {

	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		System.out.println("Digite um numero: ");
		int numero = entrada.nextInt();
		int contador = 0, contador1 = 0;
		while (contador < numero) {
			contador++;
			if (contador % 2 == 0) {
				System.out.print(contador+" ");
			}
		}
		System.out.println();
		while (contador1 < numero) {
			contador1++;
			if (contador1 % 2 != 0) {
				System.out.print(contador1+" ");
			}
		}
	}
}

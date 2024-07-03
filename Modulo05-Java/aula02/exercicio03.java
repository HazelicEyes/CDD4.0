package aula02;

import java.util.Scanner;

public class exercicio03 {
	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		System.out.println("Digite um numero: ");
		int numero = entrada.nextInt();
		
		if (numero == 1) {
			System.out.println("1 - Segunda");
		}
		else if (numero == 2) {
			System.out.println("2 - Terça");
		}
		else if (numero == 3) {
			System.out.println("3 - Quarta");
		}
		else if (numero == 4) {
			System.out.println("4 - Quinta");
		}
		else if (numero == 5) {
			System.out.println("5 - Sexta");
		}
		else if (numero == 6) {
			System.out.println("6 - Sabado");
		}
		else if (numero == 7) {
			System.out.println("7 - Domingo");
		}
		else {
			System.out.println("Numero invalido");
		}
	}
}

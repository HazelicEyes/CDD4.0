package aula02;

import java.util.Scanner;

public class exercicio02 {

	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		System.out.println("Digite o 1º numero: ");
		int n1 = entrada.nextInt();
		System.out.println("Digite o 2º numero: ");
		int n2 = entrada.nextInt();
		System.out.println("Digite o 3º numero: ");
		int n3 = entrada.nextInt();
		
		if (n1>n2) {
			if (n1>n3) {
				System.out.println("n1 é maior");
			}
			else {
				System.out.println("n3 é maior");
			}
		}
		else {
			if (n2>n3) {
				System.out.println("n2 é maior");
			}
			else {
				System.out.println("n3 é maior");
			}
		}

	}

}

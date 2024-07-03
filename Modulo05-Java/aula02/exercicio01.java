package aula02;

import java.util.Scanner;

public class exercicio01 {

	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		System.out.println("Digite um numero: ");
		int resp = entrada.nextInt();
		
		if (resp < 0) {
			System.out.println("O numero é negativo");
		}
		else {
			System.out.println("O numero é positivo");
		}
		

	}

}

package aula01;

import java.util.Scanner;

public class scannerEntrada {

	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		System.out.println("Digite um numero: ");
		double resp = entrada.nextDouble();
		System.out.println(resp);

	}

}

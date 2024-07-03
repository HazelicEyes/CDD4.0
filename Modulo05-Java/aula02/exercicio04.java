package aula02;

import java.util.Scanner;

public class exercicio04 {
	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		System.out.println("Digite ua primeira nota: ");
		double nota1 = entrada.nextDouble();
		System.out.println("Digite ua segunda nota: ");
		double nota2 = entrada.nextDouble();
		double soma = nota1 + nota2;
		double media = soma / 2;
		
		System.out.printf("A media é %s", media);
	}

}

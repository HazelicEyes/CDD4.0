package aula03_aulas_de_repeticao;

import java.util.Scanner;

public class aula02 {

	public static void main(String[] args) {
		System.out.println("Quantos alunos tem na sala? ");
		Scanner entrada = new Scanner(System.in);
		int quantidade = entrada.nextInt();
		float soma = 0;
		int contador = 1;
		while (contador <= quantidade) {
			System.out.printf("Digite a nota do %dº aluno: ", contador);
			Scanner entrada1 = new Scanner(System.in);
			soma = soma + entrada1.nextFloat();
			contador++;
		}
		float media = soma / quantidade;
		System.out.printf("A media aritmetica da sala é %.2f", media);
	}

}

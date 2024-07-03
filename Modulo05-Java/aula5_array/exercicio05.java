package aula5_array;

import java.util.Scanner;

public class exercicio05 {

	public static void main(String[] args) {
		double notas[] = new double[5];
		double soma = 0;
		Scanner entrada = new Scanner (System.in);
		for(int i = 0; i < notas.length; i++) {
			System.out.printf("Digite a nota do %dº aluno: ", i+1);
			notas[i] = entrada.nextDouble();
			soma = soma + notas[i];
		}
		double media = soma / 5;
		System.out.printf("A media da turma é %.1f", media);
	}

}

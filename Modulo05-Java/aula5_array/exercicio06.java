package aula5_array;

import java.util.Scanner;

public class exercicio06 {

	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		int a[] = new int[5];
		for(int i = 0; i < a.length; i++) {
			System.out.printf("Digite o %dº valor: ", i+1);;
			a[i] = entrada.nextInt();
		}
		for (int g:a)
			System.out.print(g+" ");

	}

}

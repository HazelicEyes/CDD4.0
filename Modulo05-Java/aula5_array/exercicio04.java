package aula5_array;

import java.util.Arrays;
import java.util.Scanner;

public class exercicio04 {

	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		int array1[] = new int[10];
		int array2[] = new int[10];
		int array3[] = new int[10];
		int array4[] = new int[10];
		for (int i=0; i < array1.length; i++) {
			System.out.printf("Preencha o array1 na posição %d: ", i+1);
			array1[i] = entrada.nextInt();
		}
		for (int i=0; i < array2.length; i++) {
			System.out.printf("Preencha o array2 na posição %d: ", i+1);
			array2[i] = entrada.nextInt();
		}
		for (int i=0; i < array3.length; i++) {
			System.out.printf("Preencha o array3 na posição %d: ", i+1);
			array3[i] = entrada.nextInt();
		}
		for (int i=0; i < array4.length; i++) {
			System.out.printf("Preencha o array4 na posição %d: ", i+1);
			array4[i] = entrada.nextInt();
		}
//	    System.out.println(Arrays.toString(array1));
//	    System.out.println(Arrays.toString(array2));
//	    System.out.println(Arrays.toString(array3));
//	    System.out.println(Arrays.toString(array4));
		for (int i:array1)
			System.out.print(i + " ");
		System.out.println();
		for (int i=0; i < array2.length; i++)
			System.out.print(array2[i] + " ");
		System.out.println();
		for (int i=0; i < array3.length; i++)
			System.out.print(array3[i] + " ");
		System.out.println();
		for (int i=0; i < array4.length; i++)
			System.out.print(array4[i] + " ");

	}

}

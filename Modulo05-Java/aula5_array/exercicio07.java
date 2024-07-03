package aula5_array;

import java.util.Arrays;

public class exercicio07 {

	public static void main(String[] args) {
		int arrayAntigo[] = {20,17,22,16,36,57,80};
		int arrayNovo[] = new int[7];
		
		for (int i=6; i>=0;i--) // 1º printar na ordem reversa
			System.out.print(arrayAntigo[i]+" ");
		for (int i=6, x=0; i>=0 ; i--, x++) //2º gravar o array antigo em um novo
			arrayNovo[x] = arrayAntigo[i];
		System.out.println();
		for (int i=0; i<arrayNovo.length;i++)
			System.out.print(arrayNovo[i]+" ");
		System.out.println();
		
		Arrays.sort(arrayNovo);// 3º ordenar em ordem crescente
		for (int i=0; i<arrayNovo.length;i++) 
			System.out.print(arrayNovo[i]+" ");
		System.out.println();
		
		for (int i=0; i<arrayAntigo.length;i++) // 4º refazer o 1 sem inverter o for
			System.out.print(arrayAntigo[6-i]+" ");
	}

}

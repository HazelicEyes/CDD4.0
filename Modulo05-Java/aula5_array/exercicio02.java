package aula5_array;

public class exercicio02 {

	public static void main(String[] args) {
		int array1[] = {12,3,5,68,9,6,73,44,456,65,321};
		int array2[] = {43,42,4,8,55,21,2,45};
		
		if (array2.length > 8) {
			System.out.println("Tamanho do array2 maior que 8");
		}
		else {
			System.out.println("Tamanho do array2 menor ou igual a 8");
		}
		System.out.println("\nTamanho do Array1 = "+array1.length);
	}

}

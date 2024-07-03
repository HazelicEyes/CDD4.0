package aula03_aulas_de_repeticao;

public class aula03 {

	public static void main(String[] args) {
		int contador = 0;
		while(contador <=100) {
			contador++;
			System.out.println(contador % 2 != 0? contador:"");
		}

	}

}

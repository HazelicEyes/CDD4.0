package aula04_repeticao_for;

public class exercicio03 {

	public static void main(String[] args) {
		for(int i=0; i<100; i++) {
			if (i > 50 && i < 60) {
				continue;
			}
		System.out.println(i);
		}
	}

}

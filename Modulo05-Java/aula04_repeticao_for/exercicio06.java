package aula04_repeticao_for;

public class exercicio06 {

	public static void main(String[] args) {
		int x = 10;
		for (int i = 1; i <=50; i++) {
			if (x % 2 ==0) {
				x = x/2;
				System.out.println(x);
			}
			else {
				x = 3 * x + 1;
				System.out.println(x);
			}
		}
	}

}
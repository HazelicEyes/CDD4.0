package aula04_repeticao_for;

public class exercicio02 {
	public static void main(String[] args) {
//		for (int i=0; i<10;i++) {
//			System.out.println("ola");
//		}
		for (int i = 0; i < 100; i++) {
			if (i % 19 == 0) {
				System.out.println("Ache um numero divisivel por 19 entre x e y");
				break;
			}
		}
	}
}
